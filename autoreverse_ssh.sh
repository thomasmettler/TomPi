


autossh -M 20000 -XY -f -N -T -R 12000:localhost:22 -R 12001:localhost:5900 thomasm@lheppc46.unibe.ch
autossh -M 22000 -f -N -T -R 12300:localhost:3000 -f -N -T -R 12888:localhost:8765 thomasm@lheppc46.unibe.ch
