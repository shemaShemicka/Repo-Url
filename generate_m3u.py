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
                
                # Chistenje na URL-to (mora da zavrshuva na /c/ ili /)
                if not portal.endswith('/'):
                    portal += '/'
                
                # Ime na portalot za polesno naogjanje
                name = portal.split("//")[-1].split("/")[0]
                
                # FORMAT ZA OTT NAVIGATOR (STALKER URL)
                # Ovoj format go primoruva playerot da otvori Stalker konekcija
                stalker_url = f"stalker://{portal.replace('http://', '').replace('https://', '')}?mac={mac}"
                
                f.write(f'#EXTINF:-1, --- {name} ---\n')
                f.write(f'{stalker_url}\n')

if __name__ == "__main__":
    create_m3u()
