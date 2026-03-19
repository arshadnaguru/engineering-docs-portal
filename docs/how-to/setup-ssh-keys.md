# Set Up SSH Keys for Remote Servers

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** How-To

Configure SSH key authentication for passwordless access to remote servers.

## Step 1: Generate an SSH Key Pair

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```

Press Enter to accept the default file location (`~/.ssh/id_ed25519`). Optionally set a passphrase.

## Step 2: Copy the Public Key to the Server

```bash
ssh-copy-id user@server-ip
```

Or manually:

```bash
cat ~/.ssh/id_ed25519.pub | ssh user@server-ip "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

## Step 3: Test the Connection

```bash
ssh user@server-ip
# Should connect without asking for a password
```

## Step 4: Create SSH Config (Optional)

Create `~/.ssh/config`:

```
Host render-node-1
    HostName 192.168.1.101
    User studio
    IdentityFile ~/.ssh/id_ed25519

Host render-node-2
    HostName 192.168.1.102
    User studio
    IdentityFile ~/.ssh/id_ed25519
```

Now connect with: `ssh render-node-1`

## Security Best Practices

- Use Ed25519 keys (more secure than RSA)
- Always set a passphrase on your private key
- Never share your private key (`id_ed25519`) — only the `.pub` file
- Disable password authentication on servers once keys are set up

---

*Last updated: March 2026 · Author: Arshad Naguru*
