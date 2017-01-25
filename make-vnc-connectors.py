"""
Password for all VNC connections is "openai".
"""

import os

TEMPLATE = open('template.xml', 'r').read()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=None)
    parser.add_argument('-ip', '--ip', default='127.0.0.1', 
                        help='IP address of the VNC server [127.0.0.1]')
    parser.add_argument('-pr', '--port-range', default='5900:5903', 
                        help='range of ports you want to make connectors for [5900:5903]')
    args = parser.parse_args()

    i = args.port_range.index(':')
    assert i > 0
    pr = [int(args.port_range[:i]), int(args.port_range[i+1:])]
    pr = map(int, pr)

    ddir = 'vnc-connectors-for-%s:[%i:%i]' % (args.ip, pr[0], pr[1])
    if not os.path.exists(ddir):
        os.makedirs(ddir)

    for p in range(pr[0], pr[1] + 1):
        f = os.path.join(ddir, 'vnc-%s:%s.vncloc' % (args.ip, p))
        print('-'*100)
        print f
        with open(f, 'w+') as fout:
            tmp = TEMPLATE.replace('_IP', args.ip)
            tmp = tmp.replace('_PORT', str(p))
            print '-'*100
            print tmp
            fout.write(tmp + '\n')
                       