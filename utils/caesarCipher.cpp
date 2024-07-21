
#include <iostream>
using namespace std ;


string encrypt(const string& text, int key) {
	string result = "" ;
	
	for (char c : text) {
		if (isalpha(c)) {
			char offset = isupper(c) ? 'A' : 'a' ;			//Check uppercase/lowercase.
			
			result += (c - offset + key) % 26 + offset ;	//Encrypt!
		} else	
			result += c ;									//If not an alphabet, then leave as is.
	}
	return result ;
}


string decrypt(const string& text, int key) {
	return encrypt(text, 26 - (key % 26) ) ;				//Simply, use the negative key.
}


int main() {
	// string text ;
	// getline(cin, text) ;					// Works !! But how/why ??
	// int key = 27 ;
	// cout << encrypt (text, key) << '\n' << decrypt(text, key) << '\n' ;
	return 0 ;
}
