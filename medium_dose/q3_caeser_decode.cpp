#include <iostream>
#include <string>
#include <cctype>
using namespace std;

string decode(string message) {
    string result = "";
    
    for (int i = 0; i < message.length(); i++) {
        char c = toupper(message[i]); // Convert to uppercase first
        int original = (c - 'A' - (i + 1)) % 26;// Shift back by position (1-indexed)
        if (original < 0) original += 26;// Handle negative modulo
        result += (char)(original + 'A');// Append decoded character
    }
    
    return result;
}

int main() {
    string message;
    
    cout << "Enter encrypted message: ";
    cin >> message;
    
    cout << "Decoded message: " << decode(message) << endl;
    
    return 0;
}