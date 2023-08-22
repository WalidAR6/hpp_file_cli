import sys

if len(sys.argv) < 3:
    exit()

file_name = sys.argv[1]
class_name = sys.argv[2]

str = """#ifndef {DefineName}_H
# define {DefineName}_H

# include <iostream>

class {ClassName}
{
    private:
        std::string name;
    public:
        {ClassName}();
        {ClassName}(const {ClassName} &copy);
        {ClassName} & operator = (const {ClassName} &copy);
        ~{ClassName}();

        void        setName(std::string name);
        std::string getName();
};

#endif
"""
replace = str.replace("{DefineName}", file_name.upper())\
                .replace("{ClassName}", class_name)

with open(file_name + ".hpp", "w") as r:
    r.write(replace)
