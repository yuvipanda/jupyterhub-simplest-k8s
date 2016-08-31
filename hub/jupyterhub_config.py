import os

c.JupyterHub.spawner_class = 'kubespawner.KubeSpawner'

# Use the nginx based proxy, rather than the nodejs one
c.JupyterHub.proxy_cmd = '/usr/local/bin/nchp'
c.JupyterHub.ip = '0.0.0.0'

c.KubeSpawner.kube_namespace = 'default'
c.KubeSpawner.kube_api_endpoint = 'https://kubernetes'
c.KubeSpawner.start_timeout = 60 * 5  # Upto 5 minutes, first pulls can be really slow

# Our simplest user image! Optimized to just... start, and be small!
c.KubeSpawner.singleuser_image_spec = 'yuvipanda/simple-singleuser:v1'

# The spawned containers need to be able to talk to the hub!
c.KubeSpawner.hub_ip_connect = '%s:%s' % (os.environ['HUB_SERVICE_HOST'], os.environ['HUB_SERVICE_PORT'])

# Do not use any authentication at all
c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
