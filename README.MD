# mk_FAH
### This project is _NOT_ affiliated with Folding@Home. Just a personal project.
> checkmk special agent plugin for monitoring Folding@Home slots and points without any plugin installation on hosts

### Features

- Does not require plugin installation on host
- Tracks points per day
- No external libraries

### Language(s)

- Python 3.6.9 (tested, lower may be available)

### Requirements

| Software | Version(s) | URL|
| -|-|-|
| Python 3| >=3.6.9 | [Python 3](https://www.python.org/downloads/) |
| checkmk | >= 1.6 (>= 2.0 untested) | [checkmk.com](https://checkmk.com/) |


### Instructions
> TODO: Generate .mkp file

- Place files in checkmk instance directories as identified by folder structure
- Configure hosts to use external datasource (either as only source or in addition to another agent/special agent)
- Test and activate host changes

### Resources

- [Check Mk Create Own Special Agent](https://digaround.cloud/check-mk-create-own-special-agent/)
- [checkmk documentation](https://docs.checkmk.com/latest/en/)
- [Folding@Home base telnet script](https://forums.anandtech.com/threads/folding-home-fahclient-config-control-manual-page.2574018/#post-40108202)

## Screenshots

- Services overview:
![Services generated](https://i.imgur.com/hH2IZRk.png)

- Estimated points per day:
![Points Per Day](https://i.imgur.com/P9biJKx.png)

- Slot Full output:
![Slots Full output](https://i.imgur.com/lw6ZIyO.png)