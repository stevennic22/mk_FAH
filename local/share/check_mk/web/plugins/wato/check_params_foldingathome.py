register_check_parameters(
  subgroup_networking,
  "foldingathome",
  _("Folding@Home"),
  Dictionary(
    elements = [
      ("Timeout_Alert",
        DropdownChoice(
          title=_("Alert for timeout range"),
          choices=[
            (True, _("Please alert")),
            (False, _("Do not alert")),
        ],
        default_value=False,
      )),
      ("Expiry_Alert",
        DropdownChoice(
          title=_("Alert for expiry range"),
          choices=[
            (True, _("Please alert")),
            (False, _("Do not alert")),
        ],
        default_value=False,
      )),
      ("Work_Unit_Output",
        DropdownChoice(
          title=_("Set true for full work unit output in long output."),
          choices=[
            (True, _("Long output")),
            (False, _("No output")),
        ],
        default_value=False,
      ))
    ]
  ),
  None,
  match_type = "dict"
)
