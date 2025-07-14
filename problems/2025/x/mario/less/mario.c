#include <cs50.h>
#include <stdio.h>

void mario(int height);

int main(void) {
    int height;
    do {
        height = get_int("Height: ");
    } while (height < 1 || height > 8);
    mario(height);
}


void mario(int height) {
    for (int row = 1; row <= height; row++) {
        //prints a space
        for (int space = 0; space < height - row; space++) {
            printf(" ");
        }
        //print hashes
        for (int hash = 0; hash < row; hash++) {
            printf("#");
        }
        printf("\n");
    }
}
