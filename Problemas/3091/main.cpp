#include <iostream>

int main() {
    int a;
    int b;
    int x;

    std::cin >> a;
    std::cin >> b;

    x = a % b;

    std::cout << std::to_string(x) + "\n";
    return 0;
}
