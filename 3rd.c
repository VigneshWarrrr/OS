#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <fcntl.h>

#define BUFF_SIZE 1024

int main(void)
{
int src_fd, dest_fd;
ssize_t bytes_read;
char buffer[BUFF_SIZE];
char source[100], dest[100];


printf("Enter Source File name: ");
scanf("%99s", source);

printf("Enter destination File name: ");
scanf("%99s", dest);

src_fd = open(source, O_RDONLY);

if (src_fd == -1) {
    perror("Error opening source file");
    exit(1);
}

dest_fd = open(dest, O_WRONLY | O_CREAT | O_TRUNC, 0644);

if (dest_fd == -1) {
    perror("Error opening destination file");
    close(src_fd);
    exit(1);
}

while ((bytes_read = read(src_fd, buffer, BUFF_SIZE)) > 0) {
    ssize_t bytes_written = 0;

    while (bytes_written < bytes_read) {
        ssize_t result = write(dest_fd, buffer + bytes_written,
                               bytes_read - bytes_written);

        if (result == -1) {
            perror("Error writing to destination file");
            close(src_fd);
            close(dest_fd);
            exit(1);
        }

        bytes_written += result;
    }
}

if (bytes_read == -1) {
    perror("Error reading source file");
    close(src_fd);
    close(dest_fd);
    exit(1);
}

printf("Files copied successfully.\n");

close(src_fd);
close(dest_fd);

return 0;

}
