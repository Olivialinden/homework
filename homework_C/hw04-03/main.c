/******************************************************************************

•
Create a structure containing two fields, one is integer with name of size, second is a pointer of character. Name that type
of
structure as " MyString_t
•
Write a function regarding these items:
•
Return type is
boolean
•
First input argument is a pointer of char, second argument is a pointer of
MyString_t ", third argument is in type of size_t " with name of length
•
If the first or the second
arg were empty returns false, else if the pointer inside the second arg was empty allocate it with size of the input text in first arg , else if the pointer
inside the second arg was not empty, then reallocate it (by using memory functions for re allocating) with size of the input text in first arg.
•
Then all the contents in the first
arg must be copied to the pointer inside the second arg by using memory functions
•
This must be done to all the first "length" cells inside the second
arg
•
Create an instance of
arrays of MyString_t " with size of 5 with name of " array_output
•
Execute that functions with these
examples:
•
("I am prosperous
0", array_out , -->
•
("I am happy
0", array_out , -->

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef struct {
    int size;
    char *data;
} MyString_t;

bool processString(const char *input, MyString_t *output, int count) {
      
    

// Check if input or output pointer is empty所有的指针都要检查看是否指向某处
    if (input == NULL || output == NULL) {
        return false;
    }
    
    size_t myleng = strlen(input);

   for(int i=0; i<count;i++){
        // Allocate or reallocate memory for the output string data
        if (output->data == NULL) {  //这里检查的时OUTPUT 中的DATA 的指针 ， 所有的指针都要检查
            // If the output data pointer is empty, allocate memory
            output->data = (char *)malloc((myleng + 1) * sizeof(char));
        } else {
            // If the output data pointer is not empty, reallocate memory
            char *temp = (char *)realloc(output->data, (myleng + 1) * sizeof(char));
            if (temp == NULL) {
                // Memory reallocation failed, free the existing data and return false
                free(output->data);
                return false;
            }
            output->data = temp;
        }
    
        // Check if memory allocation or reallocation was successful
        if (output->data == NULL) {
            return false;
        }
     
        // Copy the input string data to the output data buffer
        memcpy(output->data, input, myleng);
        
        // Null-terminate the copied data to create a valid C-style string
        output->data[myleng] = '\0';
    
        // Update the size field to reflect the length of the copied string
        output->size = myleng;
        output++;
   }
 

    return true;
}

int main() {
    MyString_t array_output[5];
    /*So, MyString_t array_output[5]; creates an array named array_output that
    can hold up to 5 instances of the MyString_t structure. Each element in
    this array can store information about a string,
    including its size and a pointer to the character data.
    This array can be used to store and manage multiple strings using 
    the MyString_t structure.
    */

    // Example usage of processString function
    printf("hihi");
    processString("I am prosperous\0", array_output, 5);
    processString("I am happy\0", array_output, 3);

    // Print the contents of array_output
    for (int i = 0; i < 5; i++) {
        printf("Array[%d]: size = %d, data = %s\n", i, array_output[i].size, array_output[i].data);
    }

    // Clean up memory by freeing allocated data
    for (int i = 0; i < 2; i++) {
        free(array_output[i].data);
    }

    return 0;
}



