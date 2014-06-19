-module(hello_world).
-export([hello/0, main/1]).
hello() -> io:format("Goodbye, World!~n").

main(_) -> hello().