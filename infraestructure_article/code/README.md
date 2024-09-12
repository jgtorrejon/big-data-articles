# Run Code

## Create CF Template in the Console


## Upload to bucket resources private keys
- id_rsa
- known_hosts

## Go to Each Web Server and login by ssh and Run this command
```bash
# Change to superuser
sudo su

# Run userdata to copy website
sudo cloud-init clean
sudo cloud-init init
sudo cloud-init modules --mode=config
sudo cloud-init modules --mode=final
```
