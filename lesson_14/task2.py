def stop_words(words: list):
    def out_wrapper(func):
        def in_wrapper(string: str):
            start_str = func(string).split()
            new_str = func(string)
            print(start_str)
            for w in words:
                if w in start_str:
                    new_str = new_str.replace(w, "*")
            return new_str
        return in_wrapper
    return out_wrapper

@stop_words(['pepsi', 'in'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in a his branding new BMW!"


print(create_slogan("Steve"))
