#ağ analiz etmek için paket tanımladık
#scapy yüklemek için terminale 'pip3 install scapy' yazmak gerekir  
import scapy.all as scapy
#girdileri almak için kullandık
import optparse

#1) arp_requset
#2) brodcast
#3) response

def get_user_input():
    parse_object=optparse.OptionParser()
    parse_object.add_option("-i","--ipaddress",dest="ip_address",help="Enter IP address")
    (user_input,argumenets) = parse_object.parse_args()
    
    if not user_input.ip_address:
        print("Enter IP address")

    return user_input

def scan_my_network(ip):
    arp_requset_packet = scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP())
    brodcast_requset_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff");
    #scapy.ls(scapy.Ether())
    # '/' işareti scapy de birleştirme anlamıma gelir
    combined_requset_packet = brodcast_requset_packet / arp_requset_packet
    (answerd_list,unanswer_list) = scapy.srp(combined_requset_packet,timeout=1)
    answerd_list.summary()

user_ip_address = get_user_input()
scan_my_network(user_ip_address.ip_address)
