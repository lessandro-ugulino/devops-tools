# DevOps Tools

> :warning: **I am still working on this project. I'll release the tools as soon as it's done**

## Index

- [Requirements](#requirements)
- [Ansible](#ansible)
  - [Playbook Command](#playbook-command)
- [Tools](#tools)
- [Deploy](#deploy)

## Requirements

- <a href="https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-ansible-on-macos">Ansible</a>

## Ansible

### Playbook Command

The file `deploy-role.yml` will deploy each role required to deploy this project.

### Tools

> :warning: Make sure you read the documentation before deploying the tool.

| Role Name           | Description                                                       | Documentation                               |
| ------------------- | ----------------------------------------------------------------- | ------------------------------------------- |
| ec2_scheduled       | Start/Stop EC2 with a specific tag during the morning and evening | [link](roles/ec2_scheduled/README.md)       |
| warn_volumes_unused | Report via email all volumes unused (not attached)                | [link](roles/warn_volumes_unused/README.md) |

### Deploy

Run the below Ansible playbook command.

E.g

```bash
ansible-playbook deploy -e "cf_stack=ec2_scheduled"
```

`cf_stack` = role name
