section .data
    msg db "Selamat datang di kelas alpro", 0xA ; string + newline
    len equ $ - msg

section .text
    global _start

_start:
    ; write(stdout, msg, len)
    mov rax, 1          ; syscall: write
    mov rdi, 1          ; file descriptor: stdout
    mov rsi, msg        ; pointer ke string
    mov rdx, len        ; panjang string
    syscall

    ; exit(0)
    mov rax, 60         ; syscall: exit
    xor rdi, rdi        ; return code 0
    syscall
