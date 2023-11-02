import faker
from userdata.models import UserData

fake = faker.Faker()


def create_whatsapp_account(num_accounts):
    for _ in range(num_accounts):
        UserData.objects.create(
            name=fake.name(),
            email=fake.email(),
            phone=fake.phone_number(),
            password=fake.password(),
        )


def main():
    num_accounts = int(input("Enter the number of accounts to create: "))
    create_whatsapp_account(num_accounts)
    print(f"{num_accounts} accounts created and saved.")


if __name__ == "__main__":
    main()
