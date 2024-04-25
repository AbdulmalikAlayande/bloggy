PASSWORD = "password"

EMAIL = "email"

def TOKEN_CREATE_AUTHENTICATION_FAILED_FOR_USER(email, password) -> str:
    return f"""
    Authentication Failed, Either Because The User With Email {email} and Password {password} Does Not Exist
    They Are Not Allowed To Make This Request
    """
