#include <iostream>

int main() {
    int a;
    int b;
    int x;

    std::cin >> a;
    std::cin >> b;

    x = a + b;

    std::cout << "X = " + std::to_string(x) + "\n";
    return 0;
}
