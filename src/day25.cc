#include <cmath>
#include <iostream>
#include <fstream>
#include <string>

#define BASE 5

std::string add(std::string lh, std::string rh) {
    std::string ans;
    if (rh.size() > lh.size()){
        ans.assign(lh);
        lh.assign(rh);
        rh.assign(ans);
    }
    ans.assign("");

    /* *
     * How to add two numbers?
     * */

    return 0;
}

int main(void) {
    std::ifstream infile("../inputs/day25");
    std::string line;
    std::string name;

    long int number = 0;
    char c;
    while (std::getline(infile, line)) {
        int i = 0;
        while (!(line.empty())) {
            c = line.back();

            switch (c) {
                case '2':
                    number += 2 * std::pow(BASE, i); break;
                case '1':
                    number += 1 * std::pow(BASE, i); break;
                case '0': break;
                case '-': 
                    number += -1 * std::pow(BASE, i); break;
                case '=':
                    number += -2 * std::pow(BASE, i); break;
            } 
            i++;
            line.pop_back();
        }
    }
    std::cout << number << std::endl;

    /* Now do it in reverse */
    
    int maxbase = 0;
    int num = 0;
    while (std::pow(BASE, maxbase) < number) { maxbase++; }

    std::cout << maxbase << std::endl;
}
