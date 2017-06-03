# super-duper-pancake
A OIDC Authentication Tester written for Openshift Origin

## App Specific Environment Variables

* APP_OIDC_ATTRIBS
    A Base64 encoded JSON list of mapper attributes to display

    For example `WyJwcmVmZXJyZWRfdXNlcm5hbWUiLCAibmFtZSIsICJlbWFpbCJd` would
    display `email` `name` and `preferred_username` in the JSON data returned by
    `/`
