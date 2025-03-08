import asyncio
import random

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = asyncio.Lock()

    async def deposit(self, amount):
        async with self.lock:
            print(f"Depositing {amount}...")
            await asyncio.sleep(random.uniform(1, 3))  # Simulate transaction times
            self.balance += amount
            print(f"Deposit complete. New balance: {self.balance}")

    async def withdraw(self, amount):
        async with self.lock:
            if self.balance >= amount:
                print(f"Withdrawing {amount}...")
                await asyncio.sleep(random.uniform(1, 3))
                self.balance -= amount
                print(f"Withdrawal complete. New balance: {self.balance}")
            else:
                print("Insufficient funds!")

async def main():
    account = BankAccount(balance=1000)
    transactions = [
        account.deposit(800),
        account.withdraw(250),
        account.withdraw(1050),
        account.deposit(300),
    ]
    await asyncio.gather(*transactions)
    print(f"Final balance: {account.balance}")

if __name__ == "__main__":
    asyncio.run(main())
