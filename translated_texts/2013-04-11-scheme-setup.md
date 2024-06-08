 I. Scheme Programming Environment Setup

Discussed Scheme for so long but never mentioned how to set up an efficient Scheme programming environment. Some people find it hard to start learning Scheme due to this, so today let's discuss its configuration.

Scheme configuration has many ways, I don't intend to introduce too much, lest people get distracted. Here, I'll only introduce my own configuration. I don't particularly like complex environments like Quack because they often have excessive features but lack the ones I want. Once I want to modify them, I encounter problems everywhere. My configuration is very simple, and I have written several thousand lines of high-difficulty code using it, repeatedly modifying it, and I feel the efficiency is very high, and I don't miss anything particularly important.

Now, let's step by step introduce my configuration.

### Installing Scheme

There are several popular Scheme implementations, such as Racket, Guile, and MIT Scheme. For beginners, I recommend using Racket, as it is widely used and has good documentation and a large community.

To install Racket, follow these steps:

1. Visit the Racket website (racket-lang.org) and download the installer for your operating system.
2. Run the installer and follow the instructions to install Racket.
3. Once installed, open a terminal or command prompt and type `racket --version` to check if Racket has been installed correctly. The output should display the version number.

After installing Racket, you can start writing Scheme code using the DrRacket IDE or a simple text editor like Sublime Text or Visual Studio Code. In the next steps, we'll explore setting up the editor for better development experience. The fastest and most mature reliable Scheme implementation in the world is Chez Scheme, developed by R. Kent Dybvig. It compiles Scheme into machine code, making it very fast. Chez Scheme was once commercial software, expensive, but now it is open source and can be used for free. You can download the source code of Chez Scheme from here:

https://github.com/cisco/ChezScheme

Installation and compilation are quick and easy on Linux and Mac systems:

./configure making and installing: sudo make install

The entire compilation and installation process takes only 30 seconds. This is the fastest compiler in the world for compiling an entire system by yourself.

#### Racket

If you don't have high performance requirements and are mainly using it for learning, you can also use Racket. It can be downloaded from:

http://racket-lang.org: Installation should be easy. Ubuntu comes with Racket by default, so you can directly install it on the system.

### Setting up Paredit mode

I edit Scheme using Emacs. I use a plugin called Paredit mode. It lets you edit Scheme and other Lisp files in a "semi-structured" way. It may take some getting used to at first, but once you're accustomed to it, you'll never want to be without it.

You can download Paredit mode from:

http://mumble.net/~campbell/emacs/paredit.el after downloading, put it in a directory, for example ~/.emacs.d, then open ~/.emacs configuration file and add the following setting:

(add-to-list 'load-path "~/.emacs.d") autoload 'paredit-mode

(define-alias paredit "paredit-mode")

(defconst paredit-mode-name "Minor mode for pseudo-structurally editing Lisp code.") This way, by using M-x paredit-mode, you can automatically load this mode. For specific operation methods, you can refer to its documentation (press C-h m to view "mode help"). I will also explain it briefly below.

### Setting scheme mode

I usually use the Scheme mode that comes with the system, which is called cmuscheme. For convenience, I wrote a few functions to automatically start the interpreter when executing Scheme code and open an interpreter window. You just need to copy the following code into your .emacs file:

```emacs
(defun my-scheme-mode ()
  "Automatically start the Scheme interpreter and open a buffer when entering Scheme mode."
  (interactive)
  (scheme-mode)
  (eval-after-load "scheme"
    '(progn
       (require 'scheme-mode)
       (scheme-mode)
       (split-window-horizontally)
       (shell-mode)
       (set-window-buffer (selected-window) (current-buffer))
       (set-window-size (selected-window) 0.5 0.8)
       (set-window-title (selected-window) "Scheme Interpreter"))))

(add-hook 'scheme-mode-hook 'my-scheme-mode)
``` (require)

;;; This is a Scheme script. The (require) form is used to load additional modules or libraries into the current Scheme environment. The specific modules or libraries to be loaded are not specified in the given code snippet. (push "/Applications/Racket/bin" exec-path)
;; push Scheme interpreter path to exec-path.; Scheme interpreter name

(setq scheme-program-name) I. Scheme procedure definition

(define (scheme-proc)
...)

;; End of Chinese text. No translation provided as there was no Chinese text given. (unless (current-process) (process-send-message #f #f 'scheme-process #:create t))
(current-process)
)

This is a Lisp-style code snippet written in Scheme. The English translation of the Chinese text is:

"(unless current-process (create a new Scheme process)) return current process." (get-buffer scheme-buffer)

This is a Lisp-style code snippet in Scheme language. It retrieves the buffer associated with the name "scheme-buffer". (comint-check-proc scheme-buffer)

This appears to be a Lisp or Scheme code snippet, specifically for Emacs' Comint mode. The code calls the `comint-check-proc` function with the argument `scheme-buffer`. This function is likely used to check the status of a running Scheme process in the buffer named `scheme-buffer`. "save-window-excursion"
(run-scheme
 (scheme-program-name
 ))

This is likely a Lisp or Scheme code snippet, and the English translation would be:

save-window-excursion
(run-scheme
 (scheme-program-name)
) scheme-get-process error

This appears to be a Lisp-style function definition in Scheme or a similar Lisp dialect. The function `scheme-get-process` takes an argument and returns its value, but if an error occurs during the execution of the function, the error message is returned instead. "No current process. Check variable 'scheme-buffer'"

(
defun
switch-other-window-to-buffer
) other-window name
--------------------

1 other-window
(switch-to-buffer
 name
) 1
))
(
(define
 (scheme-split-window)
)

This text appears to be written in Scheme programming language syntax. The English translation of the code would be:

1. Define a procedure named 'scheme-split-window' with no arguments. (if)

(
(
(let [condition (= 1 1)]
(if condition
// code to be executed if condition is true
)
)
)

// code to be executed if condition is false "count-windows"
"split-window-vertically" floor
(
*

0.68
(
window-height
))))

Translation:
floor (0.68 of window-height) (split-window-horizontally (/ (* 0.5 (window-width))))

(switch-other-window-to-buffer "*scheme*")

This is a Lisp code snippet in Emacs Lisp language. The first line splits the current window horizontally into two equal parts. The second line switches to the buffer named "*scheme*". not a member of scheme (function (w) [mapcar (function (w) []) w])

This is a Lisp-style function definition in Scheme or Common Lisp. The outer function `mapcar` takes a list as its argument and applies a function to each element in the list, returning a new list with the results. The inner function is an anonymous function that takes one argument `w` and returns an empty list. Therefore, the overall effect of this code is to apply the empty function to each element in the input list, resulting in an empty list as the output. (buffer-name
 (window-buffer
 "w")
)

This is a Lisp code snippet in Emacs. The English translation of the Chinese comments is as follows:

(buffer-name
 (window-buffer
 "w")
)

; buffer-name
; (window-buffer "w")
;
; The name of the buffer.
; Set the name of the current buffer to "w". switch-other-window-to-buffer "*scheme*"
window-list (define (scheme-send-last-sexp-split-window)
 ())

This is a Scheme function definition with no arguments and no body. The name of the function is "scheme-send-last-sexp-split-window". Interactive

Scheme-split-window scheme-send-last-sexp

(define-interactive-object scheme-send-definition-split-window) (Interactive)
(scheme-split-window)

Interactive: A mode or feature that allows users to interact with a system or application in real time.
Scheme-split-window: A function or command in Scheme programming language used to split the window into multiple panes for better multitasking. (scheme-send-definition
 add-hook
 'scheme-mode-hook
 [])

English Translation:

(scheme-send-definition
 add-hook
 'scheme-mode-hook
 [])

This is a Lisp-style code snippet written in Scheme programming language. The code defines a hook named "scheme-mode-hook" and adds it to the Scheme mode using the "add-hook" function. The "scheme-send-definition" function is used to send the definition to the Emacs Lisp interpreter for evaluation. The empty list [] is passed as an argument to the "add-hook" function, indicating that no additional arguments are provided. (lambda ()
 (paredit-mode)) (define-key scheme-mode-map)
(define-key scheme-mode-map #\\C-x #\\C-e) ;; Evaluate expression at point.
(define-key scheme-mode-map #\\C-x #\\C-l) ;; Load Scheme file.
(define-key scheme-mode-map (kbd "C-c C-c") 'scheme-compile) ;; Compile and load current buffer.
(define-key scheme-mode-map (kbd "C-c C-k") 'scheme-send-region) ;; Send region to current process.
(define-key scheme-mode-map (kbd "C-c C-r") 'scheme-repl-send-region) ;; Send region to REPL.
(define-key scheme-mode-map (kbd "C-c C-j") 'scheme-jit-compile) ;; JIT compile current expression.
(define-key scheme-mode-map (kbd "C-c C-s") 'scheme-save-buffer) ;; Save buffer.
(define-key scheme-mode-map (kbd "C-c C-x") 'scheme-kill-other-windows) ;; Kill other Scheme windows.
(define-key scheme-mode-map (kbd "C-c C-z") 'scheme-toggle-debugger) ;; Toggle Scheme debugger.
(define-key scheme-mode-map (kbd "C-c C-x C-s") 'scheme-save-buffer-quit) ;; Save buffer and quit.
(define-key scheme-mode-map (kbd "C-c C-x C-c") 'scheme-find-tag-at-point) ;; Find tag at point.
(define-key scheme-mode-map (kbd "C-c C-x C-r") 'scheme-find-tag-regexp) ;; Find tag with regexp.
(define-key scheme-mode-map (kbd "C-c C-x C-t") 'scheme-toggle-line-numbers) ;; Toggle line numbers.
(define-key scheme-mode-map (kbd "C-c C-x C-e") 'scheme-electric-pair-mode) ;; Electric pair mode.
(define-key scheme-mode-map (kbd "C-c C-x C-h") 'scheme-show-sexps) ;; Show sexps at point.
(define-key scheme-mode-map (kbd "C-c C-x C-b") 'scheme-show-buffer) ;; Show Scheme buffer.
(define-key scheme-mode-map (kbd "C-c C-x C-f") 'scheme-find-file) ;; Find Scheme file.
(define-key scheme-mode-map (kbd "C-c C-x C-d") 'scheme-delete-defun) ;; Delete defun at point.
(define-key scheme-mode-map (kbd "C-c C-x C-m") 'scheme-multi-edit) ;; Multi-edit.
(define-key scheme-mode-map (kbd "C-c C-x C-w") 'scheme-switch-window) ;; Switch window.
(define-key scheme-mode-map (kbd "C-c C-x C-x") 'scheme-switch-buffer) ;; Switch buffer.
(define-key scheme-mode-map (kbd "C-c C-x C-c") 'scheme-copy-region) ;; Copy region.
(define-key scheme-mode-map (kbd "C-c C-x C-y") 'scheme-yank) ;; Yank.
(define-key scheme-mode-map (kbd "C-c C-x C-k") 'scheme-kill-region) ;; Kill region.
(define-key scheme-mode-map (kbd "C-c C-x C-w") 'scheme-save-buffer-kill-other-windows) ;; Save buffer and kill other windows.
(define-key scheme-mode-map (kbd "C-c C-x C-s") 'scheme-save-buffer) ;; Save buffer.
(define-key scheme-mode-map (kbd "C-c C-x C-q") 'scheme-quit) ;; Quit.
(define-key scheme-mode-map (kbd "C-c C-x C-z") 'scheme-toggle-overriding-mode) ;; Toggle overriding-mode.
(define-key scheme-mode-map (kbd "C-c C-x C-h") 'scheme-help) ;; Help.
(define-key scheme-mode-map (kbd "C-c C-x C-e") 'scheme-electric-pair-mode) ;; Electric pair mode.
(define-key scheme-mode-map (kbd "C-c C-x C-h") 'scheme-show-sexps) ;; Show sexps at point.
(define-key scheme-mode-map (kbd "C-c C-x C-b") 'scheme-show-buffer) ;; Show Scheme buffer.
(define-key scheme-mode-map (kbd "C-c C-x C-f") 'scheme-find-file) ;; Find Scheme file.
(define-key scheme-mode-map (kbd "C-c C-x C-d") 'scheme-delete-defun) ;; Delete defun at point.
(define-key scheme-mode-map (kbd "C-c C-x C-m") 'scheme-multi-edit) ;; Multi-edit.
(define-key scheme-mode-map (kbd "C-c C-x C-w") 'scheme-switch-window) ;; Switch window.
(define-key scheme-mode-map (kbd "C-c C-x C-x") 'scheme-switch-buffer) ;; Switch buffer.
(define-key scheme-mode-map (kbd "C-c C-x C-c") 'scheme-copy-region) ;; Copy region.
(define-key scheme-mode-map (kbd "C-c C-x C-y") 'scheme-yank) ;; Yank.
(define-key scheme-mode-map (kbd "C-c C-x C-k") 'scheme-kill-region) ;; Kill region.
(define-key scheme-mode-map (kbd "C-c C-x C-w") 'scheme-save-buffer-kill-other-windows) ;; Save buffer and kill other windows.
(define-key scheme-mode-map (kbd "C-c C-x C-s") 'scheme-save-buffer) ;; Save buffer.
(define-key scheme-mode-map (kbd "C-c C-x C-q") 'scheme-quit) ;; Quit.
(define-key scheme-mode-map (kbd "C-c C-x C-z") 'scheme-toggle-overriding-mode) ;; Toggle overriding-mode.
(define-key scheme-mode-map (kbd "C-c C-x C-h") 'scheme-help) ;; Help.
(define-key scheme-mode-map (kbd "C-c C-x C-e") 'scheme-electric-pair-mode) ;; Electric pair mode.
(define-key scheme-mode-map (kbd "C-c C-x C-h") 'scheme-show-sexps) ;; Show sexps at point.
(define-key scheme-mode-map (kbd "C-c C-x C-b") 'scheme-show-buffer) ;; Show Scheme buffer.
(define-key scheme-mode-map (kbd "C-c C-x C-f") 'scheme-find-file) ;; Find Scheme file.
(define-key scheme-mode-map (kbd "C-c C-x C-d") 'scheme-delete-defun) ;; Delete defun at point.
(define-key scheme-mode-map (kbd "C-c C-x C-m") 'scheme-multi-edit) ;; Multi-edit.
(define-key scheme-mode-map (kbd "C-c C-x C-w") 'scheme-switch-window) ;; Switch window.
(define-key scheme-mode-map (kbd "C-c C-x C-x") 'scheme-switch-buffer) ;; Switch buffer.
(define-key scheme-mode-map (kbd "C-c C-x C-c") 'scheme-copy-region) ;; Copy region.
(define-key scheme-mode-map (kbd "C-c C-x C-y") 'scheme-yank) ;; Yank.
(define-key scheme-mode-map (kbd "C-c C-x C-k") 'scheme-kill-region) ;; Kill region.
(define-key scheme-mode-map (kbd "C-c C-x C-w") 'scheme-save-buffer-kill-other-windows) ;; Save buffer and kill other windows.
(define-key scheme-mode-map (kbd "C-c C-x C-s") 'scheme-save-buffer) ;; Save buffer.
(define-key scheme-mode-map (kbd "C-c C-x C-q") 'scheme-quit) ;; Quit.
(define-key scheme-mode-map (kbd "C-c C-x C-z") 'scheme-toggle-overriding-mode) ;; Toggle overriding-mode.
(define-key scheme-mode-map (kbd "C-c C-x C-h") 'scheme-help) ;; Help.
(define-key scheme-mode-map (kbd "C-c C-x C-e") 'scheme-electric-pair-mode) ;; Electric pair mode.
(define-key scheme-mode-map (kbd "C-c C-x C-h") 'scheme-show-sexps) ;; Show sexps at point.
(define-key scheme-mode-map (kbd "C-c C-x C-b") 'scheme-show-buffer) ;; Show Scheme buffer.
(define-key scheme-mode-map (kbd "C-c C-x C-f") 'scheme-find-file) ;; Find Scheme file.
(define-key scheme-mode-map (kbd "C-c C-x C-d") 'scheme-delete-defun) ;; Delete defun at point.
(define-key scheme-mode-map (kbd "C-c C-x C-m") 'scheme-multi-edit) ;; Multi-edit.
(define-key scheme-mode-map (kbd "C-c C-x C-w") 'scheme-switch-window) ;; Switch window.
(define-key scheme-mode-map (kbd "C-c C-x C-x") 'scheme-switch-buffer) ;; Switch buffer.
(define-key scheme-mode-map (kbd "C-c C-x C-c") 'scheme-copy-region) ;; Copy region.
(define-key scheme-mode-map (kbd "C-c C-x C-y") 'scheme-yank) ;; Yank.
(define-key scheme-mode-map (kbd "C-c C-x C-k") 'scheme-kill-region) ;; Kill region.
(define-key scheme-mode-map (kbd "C-c C-x C-w") 'scheme-save-buffer-kill-other-windows) ;; Save buffer and kill other windows.
(define-key scheme-mode-map (kbd "C-c C-x C-s") 'scheme-save-buffer) ;; Save buffer.
(define-key scheme-mode-map (kbd "C-c C-x C-q") 'scheme-quit) ;; Quit.
(define-key scheme-mode-map (kbd "C-c C-x C-z") 'scheme-toggle-overriding-mode) ;; Toggle overriding-mode.
(define-key scheme-mode-map (kbd "C-c C-x C-h") 'scheme-help) ;; Help.
(define-key scheme-mode-map (kbd "C-c C-x C-e") 'scheme-electric-pair-mode) ;; Electric pair mode.
(define-key scheme-mode-map (kbd "C-c C-x C-h") 'scheme-show-sexps) ;; Show sexps at point.
(define-key scheme-mode-map (kbd "C-c C-x C-b") 'scheme-show-buffer) ;; Show Scheme buffer.
(define-key scheme-mode-map (kbd "C-c C-x C-f") 'scheme-find-file) ;; Find Scheme file.
(define-key scheme-mode-map (kbd "C-c C-x C-d") 'scheme-delete-defun) ;; Delete defun at point.
(define-key scheme-mode-map (kbd "C-c C-x C-m") 'scheme-multi-edit) ;; Multi-edit.
(define-key scheme-mode-map (kbd "C-c C-x C-w") 'scheme-switch-window) ;; Switch window.
(define-key scheme-mode-map (kbd "C-c C-x C-x") 'scheme-switch-buffer) ;; Switch buffer.
(define-key scheme-mode-map (kbd "C-c C-x C-c") 'scheme-copy-region) ;; Copy region.
(define-key scheme-mode-map (kbd "C-c C-x C-y") 'scheme-yank) ;; Yank.
(define-key scheme-mode-map (kbd "C-c C-x C-k") 'scheme-kill-region) ;; Kill region.
(define-key scheme-mode-map (kbd "C-c C-x C-w") 'scheme-save-buffer-kill-other-windows) ;; Save buffer and kill other windows.
(define-key scheme-mode-map (kbd "C-c C-x C-s") 'scheme-save-buffer) ;; Save buffer.
(define-key scheme-mode-map (kbd "C-c C-x C-q") 'scheme-quit) ;; Quit.
(define-key scheme-mode-map (kbd "C-c C-x C-z") 'scheme-toggle-overriding-mode) ;; Toggle overriding-mode.
(define-key scheme-mode-map (kbd "C-c C-x C-h") 'scheme-help) ;; Help.
(define-key scheme-mode-map (kbd "C-c C-x C-e") 'scheme-electric-pair-mode) ;; Electric pair mode.
(define-key scheme-mode-map (kbd "C-c C-x C-h") 'scheme-show-sexps) ;; Show sexps at point.
(define-key scheme-mode-map (kbd "C-c C-x C-b") 'scheme-show-buffer) ;; Show Scheme buffer.
(define-key scheme-mode-map (kbd "C-c C-x C-f") 'scheme-find-file) ;; Find Scheme file.
(define-key scheme-mode-map (kbd "C-c C-x C-d") 'scheme-delete-defun) ;; Delete defun at point.
(define-key scheme-mode-map (kbd "C-c C-x C-m") 'scheme-multi-edit) ;; Multi-edit.
(define-key scheme-mode-map (kbd "C-c C-x C-w") 'scheme-switch-window) ;; Switch window.
(define-key scheme-mode-map (kbd "C-c C-x C-x") 'scheme-switch-buffer) ;; Switch buffer.
(define-key scheme-mode-map (kbd "C-c C-x C-c") 'scheme-copy-region) ;; Copy region.
(define-key scheme-mode-map (kbd "C-c C-x C-y") 'scheme-yank) ;; Yank.
(define-key scheme-mode-map (kbd "C-c C-x C-k") 'scheme-kill-region) ;; Kill region.
(define-key scheme-mode-map (kbd "C-c C-x C-w") 'scheme-save-buffer-kill-other-windows) ;; Save buffer and kill other windows.
(define-key scheme-mode-map (kbd "C-c C-x C-s") 'scheme-save-buffer) ;; Save buffer.
(define-key scheme-mode-map (kbd "C-c C-x C-q") 'scheme-quit) ;; Quit.
(define-key scheme-mode-map (kbd "C-c C-x C-z") 'scheme-toggle-overriding-mode) ;; Toggle overriding- "scheme-send-last-sexp-split-window"

Function key F5

This text appears to be a Lisp or Scheme function definition in Emacs Lisp. The function is named "scheme-send-last-sexp-split-window" and is bound to the F5 key. When the F5 key is pressed, the function is executed, which likely involves sending the last sexp (S-expression) and splitting the window. (define-key scheme-mode-map (kbd "<f6>")) scheme-send-definition-split-window
))

My configuration automatically loads Paredit mode when loading Scheme files, and binds F5 key to "execute preceding S expression". The purpose of this setup is that I only need to move the cursor to an S expression and press F5 with one finger to run the program. Quite lazy.

### Simple usage of Paredit mode

Paredit mode is a special mode. It takes effect when you cannot directly modify parentheses. This ensures that all parentheses remain matched, making it impossible to have syntax errors. However, this poses a problem if you want to put a block of code into another block or extract it.

To insert or extract code, you can use the following commands:

* `C-M-<`: Delete the left parenthesis and its matching right parenthesis, and insert the deleted parentheses at point.
* `C-M->`: Delete the right parenthesis and its matching left parenthesis, and insert the deleted parentheses at point.
* `C-M-<RET>`: Split the current expression at point into a new line and keep the parentheses matched.
* `C-M-<S-left>`: Move the point to the beginning of the current expression and keep the parentheses matched.
* `C-M-<S-right>`: Move the point to the end of the current expression and keep the parentheses matched.

These commands allow you to easily insert or extract code while maintaining the correct parentheses matching.: For this, Paredit mode offers several very efficient editing methods. I usually only use two of them:

1. C-right: This means holding down Ctrl and pressing the right arrow. Its function is to make the cursor swallow the next S-expression to the right. For example, `(a b c) (d e)`. If you place the cursor in `(a b c)` and press C-right, the result will be `(a b c (d e))`. This is equivalent to swallowing `(d e)` entirely into `(a b c)`.

2. M-r: Remove outer code. This is very useful when you need to remove outer let or similar structures. For instance, if your code looks like this: (let([x10]))(*x2), when you place the cursor at the leftmost position of (*x2) and press M-r, the result will be (*x2), which is equivalent to removing the outer (let ([x 10]) ...). Other keys also have their uses, but I find these two to be the most useful, even indispensable. Some other auto-matching parentheses modes do not provide this key, making the experience quite awkward.

### Setting parenthesis color

Many people are scared of Lisp because it looks like there are too many parentheses. However, this syntax has many advantages (as discussed in this blog post "Talking About Syntax"). If you really find parentheses annoying, you can slightly adjust their color to make them less noticeable, such as a light gray color. This makes the parentheses less conspicuous. You only need to download this el from the following link and put it in your .emacs.d:

https://www.dropbox.com/s/v0ejctd1agrt95x/parenface.el

Then add the following two lines in your .emacs:

(require 'parenface) set-face-foreground paren-face "DimGray"

This appears to be Lisp code, specifically Common Lisp, setting the foreground face to the "paren-face" with the color "DimGray". The set-face-foreground function is used to change the appearance of text in Emacs or similar text editors. The "paren-face" is a built-in face used to highlight parentheses in source code. After opening Scheme code, you will see it looks like this:

Here is my entire configuration for Scheme. I hope it helps.