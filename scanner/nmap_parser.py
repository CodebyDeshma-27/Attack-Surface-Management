from lxml import etree

def parse_nmap_xml(xml_path="output/latest_scan.xml"):
    tree = etree.parse(xml_path)
    root = tree.getroot()

    results = []

    for host in root.findall("host"):
        address = host.find("address").get("addr")

        ports = host.find("ports")
        if ports is None:
            continue

        for port in ports.findall("port"):
            port_id = port.get("portid")
            protocol = port.get("protocol")

            service = port.find("service")
            service_name = service.get("name") if service is not None else "unknown"
            version = service.get("version") if service is not None else "unknown"

            results.append({
                "host": address,
                "port": port_id,
                "protocol": protocol,
                "service": service_name,
                "version": version
            })

    return results
