
c.ServerProxy.servers = {
  'tensorboard': {
    'command': ['tensorboard', '--logdir', '/home/jovyan/shared/logs', '--port', '{port}'],
    'timeout': 120,
    'launcher_entry': {
        'enabled': True,
        'title': 'tensorboard'
    }
  }
}