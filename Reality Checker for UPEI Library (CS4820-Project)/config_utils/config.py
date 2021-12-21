import configparser


def read_startup_config():
    print('read by start-up')
    config = configparser.ConfigParser()
    config.read('record-config.ini')
    print(config['PROGRESS'])
    print(config['PROGRESS']['incomplete'])
    print(config['PROGRESS']['status'])


def write_record_config():
    print('write intermediate records')
    config = configparser.ConfigParser()
    config['PROGRESS'] = {
        'incomplete': False,
        'status': 2,
        'input-file-path: ': './aaa.txt',
        'output-file-path': './bbb.txt',
        'current-index': 555,

    }
    with open('record-config.ini', 'w') as config_file:
        config.write(config_file)


def write_initial_config():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {
        'debug': True
    }

    config['START-UP'] = {
        'interrupted': 7,
        'back-up': 'disabled'
    }

    with open('config.ini', 'w') as config_file:
        config.write(config_file)


if __name__ == '__main__':
    write_initial_config()
    write_record_config()
    read_startup_config()
