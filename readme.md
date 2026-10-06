# C8K EEM GuestShell

A Cisco C8000V project using GuestShell, Python and EEM. The project covers GuestShell configuration, Python scripting and EEM integration.

## Structure

* [`guestshell.cfg`](./guestshell.cfg)
* [`backup_route.py`](./backup_route.py)
* [`eem.cfg`](./eem.cfg)
* [`Screengrabs/`](./Screengrabs/)

## GuestShell

Enter GuestShell from privileged EXEC mode:

```cisco
guestshell
```

## vi

Create the Python file:

```bash
vi backup_route.py
```

```text
i       Insert mode
Esc     Command mode
:w      Save
:q      Quit
:wq     Save and quit
:q!     Quit without saving
```

Check the file:

```bash
cat backup_route.py
```

## Python

[`backup_route.py`](./backup_route.py) checks the OSPF neighbour state.

If the neighbour is `FULL`, the script checks for a static default route and removes it if present.

If OSPF is not `FULL`, the script writes a static route.

## Verifying EEM

### Display Registered Policies

```cisco
show event manager policy registered
```

Displays the EEM policies currently registered on the device.

### Display Detailed Policy Information

```cisco
show event manager policy registered detailed <policy-name>
```

Displays detailed information about a registered EEM policy.

### Display EEM Configuration

```cisco
show running-config | section event manager
```

Displays the EEM configuration from the running configuration.

### Display EEM Event History

```cisco
show event manager history events
```

Displays the EEM event history.

