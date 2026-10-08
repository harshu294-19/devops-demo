#include <iostream>
using namespace std;

int main()
{
    int pin, enteredPin;
    int choice;
    double balance = 10000;
    double amount;

    pin = 1234;

    cout << "====================================\n";
    cout << "       ATM CARD MANAGEMENT SYSTEM\n";
    cout << "====================================\n";

    cout << "Enter your PIN: ";
    cin >> enteredPin;

    if (enteredPin != pin)
    {
        cout << "Invalid PIN! Access Denied.\n";
        return 0;
    }

    cout << "\nLogin Successful!\n";

    for (int i = 1; i <= 10; i++)
    {
        cout << "\n========== ATM MENU ==========\n";
        cout << "1. Check Balance\n";
        cout << "2. Deposit Money\n";
        cout << "3. Withdraw Money\n";
        cout << "4. Change PIN\n";
        cout << "5. Exit\n";
        cout << "==============================\n";

        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1)
        {
            cout << "Current Balance: Rs. " << balance << endl;
        }

        else if (choice == 2)
        {
            cout << "Enter amount to deposit: Rs. ";
            cin >> amount;

            if (amount > 0)
            {
                balance = balance + amount;
                cout << "Amount deposited successfully.\n";
                cout << "New Balance: Rs. " << balance << endl;
            }
            else
            {
                cout << "Invalid amount!\n";
            }
        }

        else if (choice == 3)
        {
            cout << "Enter amount to withdraw: Rs. ";
            cin >> amount;

            if (amount <= 0)
            {
                cout << "Invalid amount!\n";
            }
            else if (amount > balance)
            {
                cout << "Insufficient Balance!\n";
            }
            else
            {
                balance = balance - amount;
                cout << "Please collect your cash.\n";
                cout << "Remaining Balance: Rs. " << balance << endl;
            }
        }

        else if (choice == 4)
        {
            cout << "Enter new PIN: ";
            cin >> pin;

            cout << "PIN changed successfully.\n";
        }

        else if (choice == 5)
        {
            cout << "\nThank you for using ATM!\n";
            break;
        }

        else
        {
            cout << "Invalid choice! Please try again.\n";
        }
    }

    return 0;
}