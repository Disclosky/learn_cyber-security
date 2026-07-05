## 🔥 UFW = Uncomplicated Firewall


### Basic Commands
```bash
sudo ufw status    # Show status
sudo ufw enable	   # to Activate the firewall
sudo ufw disable   # to Trun off the firewall
sudo ufw reset     # Reset to default
```

### Rules
1. Show rules
```bash
sudo ufw status numbered
```
2. Add a new rule
```bash
sudo ufw allow 4444/tcp	       # open port 4444
sudo ufw allow 8000/tcp        # open port 8000
sudo ufw allow 9000:9005/tcp   # open range port
....
```
3. Delete a rule
```bash

sudo ufw delete allow 4444/tcp
```

### Things to noted:
- `Status: active`    → Firewall is on
- `deny (incoming)`   → All incoming connections are rejected
- `allow (outgoing)`  → All outgoing connections are allowed
- `disabled (routed)` → Can't act like a router


---
file to `reset-ufw.sh` instantly:
```bash

#!/bin/bash
sudo ufw reset
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw enable
sudo ufw status verbose
```
