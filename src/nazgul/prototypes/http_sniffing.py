import scapy.sendrecv
import scapy.layers.http


def extract_http_address(tcp_packet):
    """
    Extracts requested address from an HTTP request

    Processes a TCP packet, and if it contains an HTTP request, extracts
    and returns requested address combined of the host and full path.

    Args:
        tcp_packet: a Scapy TCP packet.

    Returns:
        String, being the combination of the host and full path from an
        HTTP request.
    """
    if tcp_packet.haslayer(scapy.layers.http.HTTPRequest):
        http_layer = tcp_packet.getlayer(scapy.layers.http.HTTPRequest)
        host = http_layer.fields['Host'].decode()
        path = http_layer.fields['Path'].decode()
        address = '{}{}\n'.format(host, path)
        return address

scapy.sendrecv.sniff(filter='tcp', prn=extract_http_address)
