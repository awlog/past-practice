#include <stdio.h>
#include <stdbool.h>

// create a simple program that reads a specific line of a txt file.

#define FILENAME_SIZE 1024
#define MAX_LINE 2048

int main()
{
    // file pointer will be used to open/ read from the file
    FILE *file;

    // used to store the filename and each line from the file
    char filename[FILENAME_SIZE];
    char buffer[MAX_LINE];

    // store the line number of the line the user wants to read from the file
    int read_line = 0;

    printf("FILE: ");
    scanf("%s", filename);

    printf("Read Line: ");
    scanf("%d", &read_line);

    // open the file in read mode
    file = fopen(filename, "r");
   
    if (file == NULL)
    {
        printf("Error opening file.\n");
        return 1;
    }

    /* keep readin ghtee file as keep_reading is true and
    keep track of the current line of the file using current_line
    */
    bool keep_reading = true;
    int current_line = 1;
    do
    {
        fgets(buffer, MAX_LINE, file);
        
        if (feof(file))
        {
            keep_reading = false;
            printf("File %d lines.\n", current_line-1);
            printf("Couldn't find the line %d.\n", read_line);
        }
        // if we have found the line user is long for, print it out
        else if(current_line == read_line)
        {
            keep_reading = false;
            printf("Line:\n%s", buffer);
        }

        current_line++;
  
    }while (keep_reading);

    fclose(file);
  
    return 0;
}