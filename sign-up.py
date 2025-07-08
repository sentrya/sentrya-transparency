def registration():
  hashed_password = generate_password_hash(register_form.password.data, method="pbkdf2:sha256", salt_length=12)
  generated_code = generate_code()
  code_expiration = (datetime.datetime.utcnow() + datetime.timedelta(minutes=10)).isoformat()
  new_user = User(first_name=register_form.first_name.data.title(),
                  last_name=register_form.last_name.data.title(),
                  email=register_form.email.data.lower(),
                  password=hashed_password,
                  paid="No",
                  register_date=datetime.datetime.now().strftime("%d/%m/%Y"),
                  thread_finished="No",
                  confirmation_code=generated_code,
                  confirmed_email="No",
                  confirmation_code_expiration=code_expiration,
                  selected_plan="Free",
                  inbox_sealed="No",
                  promo_code=register_form.promo_code.data or None)


def google_registration():
  characters = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(secrets.choice(characters) for _ in range(16))
  hashed_password = generate_password_hash(password, method="pbkdf2:sha256", salt_length=12)
  refresh_token = credentials.refresh_token
  new_user = User(first_name=userinfo.get("given_name"),
                  last_name=userinfo.get("family_name"),
                  email=userinfo.get("email"),
                  password=hashed_password,
                  paid="No",
                  register_date=datetime.datetime.now().strftime("%d/%m/%Y"),
                  access_token=fernet.encrypt(refresh_token.encode()),
                  thread_finished="No",
                  confirmed_email="Yes",
                  selected_plan="Free",
                  inbox_sealed="No",
                  google_signup="Yes")
