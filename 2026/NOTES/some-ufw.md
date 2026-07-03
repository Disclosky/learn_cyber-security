## 🔥 UFW = Uncomplicated Firewall

---

Things to noted:
Status: active		Firewall is on ✅
deny (incoming)		All INCOMING connections are rejected 🚫
allow (outgoing)	All OUTGOING connections are allowd✅
disabled (routed)	

Basic Commands:
```bash
sudo ufw status 	     # Show status
sudo ufw enable		     # to Activate the firewall
sudo ufw disable	     # to Trun off the firewall
sudo ufw reset		     # Reset to default```

Rules
1. Show Rules
```bash
sudo ufw status numbered```

2. Add a new rule
```
sudo ufw allow 4444/tcp      # Buka port 4444
sudo ufw allow 8000/tcp      # Buka port 8000
sudo ufw allow 9000:9005/tcp # Buka range port
....```

3. Delete a rule
```bash

sudo ufw delete allow 4444/tcp```


file to reset-ufw.sh instantly:
```bash

#!/bin/bash
sudo ufw reset
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw enable
sudo ufw status verbose
```
