"""Build a single-page, editable draw.io diagram from a local JSON model."""
import argparse
import json
from pathlib import Path
from xml.etree import ElementTree as ET


NODE_STYLE = {
    "process": "rounded=0;fillColor=#e8f0fb;strokeColor=#335d91;",
    "decision": "rhombus;fillColor=#fff1cb;strokeColor=#8b640e;",
    "terminal": "rounded=1;arcSize=40;fillColor=#e6f4eb;strokeColor=#2c6747;",
}
TEXT_STYLE = "html=0;whiteSpace=wrap;fontSize=14;fontColor=#172b3a;"
EDGE_STYLE = "edgeStyle=orthogonalEdgeStyle;endArrow=block;endFill=1;strokeColor=#355268;"


def required_text(record, key, context):
    value = record.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{context}: {key} må være en tekstverdi.")
    return value


def records(model, key, default=None):
    items = model.get(key, default)
    if not isinstance(items, list) or any(not isinstance(item, dict) for item in items):
        raise ValueError(f"{key} må være en liste med JSON-objekter.")
    return items


def add_node(root, node, node_id, context):
    label = required_text(node, "label", context)
    kind = node.get("kind", "process")
    if not isinstance(kind, str) or kind not in NODE_STYLE:
        raise ValueError(f"{context}: bruk process, decision eller terminal for kind.")

    geometry = {"as": "geometry"}
    for key, default in (("x", None), ("y", None), ("width", 180), ("height", 64)):
        value = node.get(key, default)
        if type(value) is not int or (key in {"width", "height"} and value <= 0):
            raise ValueError(f"{context}: {key} må være et gyldig heltall.")
        geometry[key] = str(value)
    cell = ET.SubElement(root, "mxCell", id=node_id, value=label,
                         vertex="1", parent="1", style=NODE_STYLE[kind] + TEXT_STYLE)
    ET.SubElement(cell, "mxGeometry", geometry)


def build(model):
    if not isinstance(model, dict):
        raise ValueError("Modellen må være et JSON-objekt.")
    title = required_text(model, "title", "Diagram")
    nodes = records(model, "nodes")
    if not nodes:
        raise ValueError("Diagrammet trenger minst én node.")

    page_file = ET.Element("mxfile", compressed="false")
    page = ET.SubElement(page_file, "diagram", id="page-1", name=title)
    graph = ET.SubElement(page, "mxGraphModel", grid="1", gridSize="10")
    root = ET.SubElement(graph, "root")
    ET.SubElement(root, "mxCell", id="0")
    ET.SubElement(root, "mxCell", id="1", parent="0")

    node_ids = {}
    for index, node in enumerate(nodes, start=1):
        identifier = required_text(node, "id", f"Node {index}")
        if identifier in node_ids:
            raise ValueError(f"ID-en {identifier!r} er brukt flere ganger.")
        node_ids[identifier] = f"node-{identifier}"
        add_node(root, node, node_ids[identifier], f"Node {identifier!r}")

    for index, edge in enumerate(records(model, "edges", []), start=1):
        context = f"Pil {index}"
        source = required_text(edge, "from", context)
        target = required_text(edge, "to", context)
        if source not in node_ids or target not in node_ids:
            raise ValueError(f"{context}: {source!r} og {target!r} må vise til kjente noder.")
        label = edge.get("label", "")
        if not isinstance(label, str):
            raise ValueError(f"{context}: label må være en tekstverdi.")
        cell = ET.SubElement(root, "mxCell", id=f"edge-{index}", value=label,
                             edge="1", parent="1", source=node_ids[source], target=node_ids[target],
                             style=EDGE_STYLE + TEXT_STYLE)
        ET.SubElement(cell, "mxGeometry", relative="1", **{"as": "geometry"})

    ET.indent(page_file)
    encoded = ET.tostring(page_file, encoding="utf-8", xml_declaration=True)
    ET.fromstring(encoded)
    return encoded + b"\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if args.output.suffix.lower() != ".drawio":
        parser.error("Utfilen må ha endelsen .drawio.")
    try:
        content = build(json.loads(args.model.read_text(encoding="utf-8-sig")))
        with args.output.open("xb") as output:
            output.write(content)
    except (OSError, ValueError, ET.ParseError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
