import cli

IP1 = "10.199.199.254"
cmd1 = f"ip route 0.0.0.0 0.0.0.0 {IP1}"
cmd2 = f"no {cmd1}

try:
    match1 = cli.cli("show ip ospf neighbor")

    if IP1 in match1 and "FULL" in match1:
        print("Status Full - OSPF default route loaded in routing table")

        out1 = cli.cli("show ip route")

        if "S*" in out1:
            cli.configure([cmd2])
            print("Removed static default route")
        else:
            print("No static default route found")
        out2 = cli.cli("show ip route")
        print(out2)
        print("Installed static route")

    else: 
        print("OSPF is down - Installing static default route")
        cli.configure([cmd1])
        out3 = cli.cli("show ip route")
        print(out3)
        print("Installed static route")

except Exception as e:
    print(f"Error: {e}")