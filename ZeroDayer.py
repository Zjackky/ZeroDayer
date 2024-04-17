import argparse

def parse_config(config_file):
    config = {}
    current_section = None
    with open(config_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                if line.startswith('[') and line.endswith(']'):
                    current_section = line[1:-1]
                    config[current_section] = []
                else:
                    config[current_section].append(line)
    return config

def search_config(config, name):
    for section, items in config.items():
        if name in items:
            return section
    return None

def main():
    parser = argparse.ArgumentParser(description='ZeroDayer')
    parser.add_argument('-f', '--file', type=str, help='Input file containing ICPnames')
    parser.add_argument('-n', '--name', type=str, help='Single ICPname')
    args = parser.parse_args()

    if args.file:
        config = parse_config('config.txt')
        with open(args.file, 'r',encoding="utf-8") as f:
            for name in f.read().strip().split('\n'):
                section = search_config(config, name)
                if section:
                    print(f'{section}: {name}')
                else:
                    print(f'No match found for: {name}')
    elif args.name:
        config = parse_config('config.txt')
        section = search_config(config, args.name)
        if section:
            print(f'{section}: {args.name}')
        else:
            print(f'No match found for: {args.name}')
    else:
        parser.print_help()

if __name__ == '__main__':
    print('''
    '  ███████╗███████╗██████╗  ██████╗ ██████╗  █████╗ ██╗   ██╗███████╗██████╗ 
'  ╚══███╔╝██╔════╝██╔══██╗██╔═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗
'    ███╔╝ █████╗  ██████╔╝██║   ██║██║  ██║███████║ ╚████╔╝ █████╗  ██████╔╝
'   ███╔╝  ██╔══╝  ██╔══██╗██║   ██║██║  ██║██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗
'  ███████╗███████╗██║  ██║╚██████╔╝██████╔╝██║  ██║   ██║   ███████╗██║  ██║
'  ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
'                                                                            
'                                                           - by @Zjacky 
    ''')
    main()