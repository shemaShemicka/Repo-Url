import os

def create_m3u():
    input_file = 'MacDataBase.txt'
    output_file = 'playlist.m3u'
    
    if not os.path.exists(input_file):
        return

    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        f.write('#EXTM3U\n')
        for line in lines:
            line = line.strip()
            if '|' in line:
                portal, mac = line.split('|')
                portal = portal.strip()
                mac = mac.strip()
                
                # Ime na portalot
                name = portal.split("//")[-1].split("/")[0]
                
                # Specijalen format za OTT Navigator da prepoznae deka e Stalker MAC
                f.write(f'#EXTINF:-1 tvg-name="{name}" group-title="MAC Portali", {name} (MAC: {mac})\n')
                f.write(f'#EXTMYTP:type=stalker\n')
                f.write(f'#EXTMYTP:st_mac={mac}\n')
                f.write(f'{portal}\n')

if __name__ == "__main__":
    create_m3u()
