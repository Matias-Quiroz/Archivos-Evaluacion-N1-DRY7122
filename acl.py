acl = int (input (" Ingrese el número de ACL ipv4: "))
if acl >=1 and acl <=99:
    print ("Esta es una ACL ipv4 standar")
elif acl >=100 and acl <=199:
    print ("Esta es una ACL ipv4 extendida")
else:
    print ("Ingrese una ACL valida")