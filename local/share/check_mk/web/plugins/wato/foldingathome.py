#!/usr/bin/python

#import required to register agent
from cmk.gui.plugins.wato import (
    IndividualOrStoredPassword,
    RulespecGroup,
    monitoring_macro_help,
    rulespec_group_registry,
    rulespec_registry,
    HostRulespec,
)

#import structure where special agent will be registered
from cmk.gui.plugins.wato.datasource_programs import RulespecGroupDatasourcePrograms

#Some WATO form definition, to ask user for port number
def _valuespec_special_agent_foldingathome():
    return Dictionary(
        title=_("foldingathome"),
        help=_("The port that Folding@Home is listening on."),
        optional_keys=[],
        elements=[
            ("port", TextAscii(title=_("Port to connect to"), default_value='36330', allow_empty=False)),
            ('auth', TextAscii(title=_("Telnet password (Leave blank for no password)"), allow_empty=True)),
        ],
    )


#In that piece of code we registering Special Agent
rulespec_registry.register(
    HostRulespec(
        group=RulespecGroupDatasourcePrograms,
        #IMPORTANT, name must follow special_agents:<name>, 
        #where filename of our special agent located in path local/share/check_mk/agents/special/ is  agent_<name>
        name="special_agents:foldingathome",
        valuespec=_valuespec_special_agent_foldingathome,
    ))
