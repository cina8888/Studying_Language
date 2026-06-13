#include <iostream>
#include <cctype>

using namespace std;

void check(int argc, char **argv) {
    if (argc < 2){
        cout << "No input";
    }else if (argc > 2) {
        cout << "There are more than 1 value input";
    } else {
        if (argv[1][0] != '0' ) {
            cout << "First perfix should be '0'";
        }   else if (tolower(argv[1][1]) != 'x') {
                cout << "Second prefix should be 'x' or 'X'";
        }   else if (argv[1][3] == '\0') {
                cout << "No decimal";
        }
        for (char *p = argv[1] + 2; *p != '\0'; p++) {
            if (!(isdigit(*p) || (tolower(*p) >= 'a' && tolower(*p) <= 'f'))) {
                cout << "Invalid Hexdecimal";
                return;
            }
        }
        cout << "Got valid hexadecimal value: " << argv[1];
    }
}


int main(int argc, char **argv) {
    check(argc, argv);
    return 0;
}