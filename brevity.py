# coding=utf-8
from __future__ import unicode_literals, print_function
import re
import sys
import warnings

if sys.version < '3':
    pass
else:
    xrange = range

TLDS = ['aaa', 'aarp', 'abarth', 'abb', 'abbott', 'abbvie', 'abc', 'able', 'abogado', 'abudhabi', 'ac', 'academy', 'accenture', 'accountant', 'accountants', 'aco', 'active', 'actor', 'ad', 'adac', 'ads', 'adult', 'ae', 'aeg', 'aero', 'aetna', 'af', 'afamilycompany', 'afl', 'africa', 'ag', 'agakhan', 'agency', 'ai', 'aig', 'aigo', 'airbus', 'airforce', 'airtel', 'akdn', 'al', 'alfaromeo', 'alibaba', 'alipay', 'allfinanz', 'allstate', 'ally', 'alsace', 'alstom', 'am', 'americanexpress', 'americanfamily', 'amex', 'amfam', 'amica', 'amsterdam', 'analytics', 'android', 'anquan', 'anz', 'ao', 'aol', 'apartments', 'app', 'apple', 'aq', 'aquarelle', 'ar', 'arab', 'aramco', 'archi', 'army', 'arpa', 'art', 'arte', 'as', 'asda', 'asia', 'associates', 'at', 'athleta', 'attorney', 'au', 'auction', 'audi', 'audible', 'audio', 'auspost', 'author', 'auto', 'autos', 'avianca', 'aw', 'aws', 'ax', 'axa', 'az', 'azure', 'ba', 'baby', 'baidu', 'banamex', 'bananarepublic', 'band', 'bank', 'bar', 'barcelona', 'barclaycard', 'barclays', 'barefoot', 'bargains', 'baseball', 'basketball', 'bauhaus', 'bayern', 'bb', 'bbc', 'bbt', 'bbva', 'bcg', 'bcn', 'bd', 'be', 'beats', 'beauty', 'beer', 'bentley', 'berlin', 'best', 'bestbuy', 'bet', 'bf', 'bg', 'bh', 'bharti', 'bi', 'bible', 'bid', 'bike', 'bing', 'bingo', 'bio', 'biz', 'bj', 'black', 'blackfriday', 'blanco', 'blockbuster', 'blog', 'bloomberg', 'blue', 'bm', 'bms', 'bmw', 'bn', 'bnl', 'bnpparibas', 'bo', 'boats', 'boehringer', 'bofa', 'bom', 'bond', 'boo', 'book', 'booking', 'boots', 'bosch', 'bostik', 'boston', 'bot', 'boutique', 'box', 'br', 'bradesco', 'bridgestone', 'broadway', 'broker', 'brother', 'brussels', 'bs', 'bt', 'budapest', 'bugatti', 'build', 'builders', 'business', 'buy', 'buzz', 'bv', 'bw', 'by', 'bz', 'bzh', 'ca', 'cab', 'cafe', 'cal', 'call', 'calvinklein', 'cam', 'camera', 'camp', 'cancerresearch', 'canon', 'capetown', 'capital', 'capitalone', 'car', 'caravan', 'cards', 'care', 'career', 'careers', 'cars', 'cartier', 'casa', 'case', 'caseih', 'cash', 'casino', 'cat', 'catering', 'catholic', 'cba', 'cbn', 'cbre', 'cbs', 'cc', 'cd', 'ceb', 'center', 'ceo', 'cern', 'cf', 'cfa', 'cfd', 'cg', 'ch', 'chanel', 'channel', 'chase', 'chat', 'cheap', 'chintai', 'christmas', 'chrome', 'chrysler', 'church', 'ci', 'cipriani', 'circle', 'cisco', 'citadel', 'citi', 'citic', 'city', 'cityeats', 'ck', 'cl', 'claims', 'cleaning', 'click', 'clinic', 'clinique', 'clothing', 'cloud', 'club', 'clubmed', 'cm', 'cn', 'co', 'coach', 'codes', 'coffee', 'college', 'cologne', 'com', 'comcast', 'commbank', 'community', 'company', 'compare', 'computer', 'comsec', 'condos', 'construction', 'consulting', 'contact', 'contractors', 'cooking', 'cookingchannel', 'cool', 'coop', 'corsica', 'country', 'coupon', 'coupons', 'courses', 'cr', 'credit', 'creditcard', 'creditunion', 'cricket', 'crown', 'crs', 'cruise', 'cruises', 'csc', 'cu', 'cuisinella', 'cv', 'cw', 'cx', 'cy', 'cymru', 'cyou', 'cz', 'dabur', 'dad', 'dance', 'data', 'date', 'dating', 'datsun', 'day', 'dclk', 'dds', 'de', 'deal', 'dealer', 'deals', 'degree', 'delivery', 'dell', 'deloitte', 'delta', 'democrat', 'dental', 'dentist', 'desi', 'design', 'dev', 'dhl', 'diamonds', 'diet', 'digital', 'direct', 'directory', 'discount', 'discover', 'dish', 'diy', 'dj', 'dk', 'dm', 'dnp', 'do', 'docs', 'doctor', 'dodge', 'dog', 'doha', 'domains', 'dot', 'download', 'drive', 'dtv', 'dubai', 'duck', 'dunlop', 'duns', 'dupont', 'durban', 'dvag', 'dvr', 'dz', 'earth', 'eat', 'ec', 'eco', 'edeka', 'edu', 'education', 'ee', 'eg', 'email', 'emerck', 'energy', 'engineer', 'engineering', 'enterprises', 'epost', 'epson', 'equipment', 'er', 'ericsson', 'erni', 'es', 'esq', 'estate', 'esurance', 'et', 'etisalat', 'eu', 'eurovision', 'eus', 'events', 'everbank', 'exchange', 'expert', 'exposed', 'express', 'extraspace', 'fage', 'fail', 'fairwinds', 'faith', 'family', 'fan', 'fans', 'farm', 'farmers', 'fashion', 'fast', 'fedex', 'feedback', 'ferrari', 'ferrero', 'fi', 'fiat', 'fidelity', 'fido', 'film', 'final', 'finance', 'financial', 'fire', 'firestone', 'firmdale', 'fish', 'fishing', 'fit', 'fitness', 'fj', 'fk', 'flickr', 'flights', 'flir', 'florist', 'flowers', 'fly', 'fm', 'fo', 'foo', 'food', 'foodnetwork', 'football', 'ford', 'forex', 'forsale', 'forum', 'foundation', 'fox', 'fr', 'free', 'fresenius', 'frl', 'frogans', 'frontdoor', 'frontier', 'ftr', 'fujitsu', 'fujixerox', 'fun', 'fund', 'furniture', 'futbol', 'fyi', 'ga', 'gal', 'gallery', 'gallo', 'gallup', 'game', 'games', 'gap', 'garden', 'gb', 'gbiz', 'gd', 'gdn', 'ge', 'gea', 'gent', 'genting', 'george', 'gf', 'gg', 'ggee', 'gh', 'gi', 'gift', 'gifts', 'gives', 'giving', 'gl', 'glade', 'glass', 'gle', 'global', 'globo', 'gm', 'gmail', 'gmbh', 'gmo', 'gmx', 'gn', 'godaddy', 'gold', 'goldpoint', 'golf', 'goo', 'goodhands', 'goodyear', 'goog', 'google', 'gop', 'got', 'gov', 'gp', 'gq', 'gr', 'grainger', 'graphics', 'gratis', 'green', 'gripe', 'grocery', 'group', 'gs', 'gt', 'gu', 'guardian', 'gucci', 'guge', 'guide', 'guitars', 'guru', 'gw', 'gy', 'hair', 'hamburg', 'hangout', 'haus', 'hbo', 'hdfc', 'hdfcbank', 'health', 'healthcare', 'help', 'helsinki', 'here', 'hermes', 'hgtv', 'hiphop', 'hisamitsu', 'hitachi', 'hiv', 'hk', 'hkt', 'hm', 'hn', 'hockey', 'holdings', 'holiday', 'homedepot', 'homegoods', 'homes', 'homesense', 'honda', 'honeywell', 'horse', 'hospital', 'host', 'hosting', 'hot', 'hoteles', 'hotels', 'hotmail', 'house', 'how', 'hr', 'hsbc', 'ht', 'hu', 'hughes', 'hyatt', 'hyundai', 'ibm', 'icbc', 'ice', 'icu', 'id', 'ie', 'ieee', 'ifm', 'ikano', 'il', 'im', 'imamat', 'imdb', 'immo', 'immobilien', 'in', 'industries', 'infiniti', 'info', 'ing', 'ink', 'institute', 'insurance', 'insure', 'int', 'intel', 'international', 'intuit', 'investments', 'io', 'ipiranga', 'iq', 'ir', 'irish', 'is', 'iselect', 'ismaili', 'ist', 'istanbul', 'it', 'itau', 'itv', 'iveco', 'iwc', 'jaguar', 'java', 'jcb', 'jcp', 'je', 'jeep', 'jetzt', 'jewelry', 'jio', 'jlc', 'jll', 'jm', 'jmp', 'jnj', 'jo', 'jobs', 'joburg', 'jot', 'joy', 'jp', 'jpmorgan', 'jprs', 'juegos', 'juniper', 'kaufen', 'kddi', 'ke', 'kerryhotels', 'kerrylogistics', 'kerryproperties', 'kfh', 'kg', 'kh', 'ki', 'kia', 'kim', 'kinder', 'kindle', 'kitchen', 'kiwi', 'km', 'kn', 'koeln', 'komatsu', 'kosher', 'kp', 'kpmg', 'kpn', 'kr', 'krd', 'kred', 'kuokgroup', 'kw', 'ky', 'kyoto', 'kz', 'la', 'lacaixa', 'ladbrokes', 'lamborghini', 'lamer', 'lancaster', 'lancia', 'lancome', 'land', 'landrover', 'lanxess', 'lasalle', 'lat', 'latino', 'latrobe', 'law', 'lawyer', 'lb', 'lc', 'lds', 'lease', 'leclerc', 'lefrak', 'legal', 'lego', 'lexus', 'lgbt', 'li', 'liaison', 'lidl', 'life', 'lifeinsurance', 'lifestyle', 'lighting', 'like', 'lilly', 'limited', 'limo', 'lincoln', 'linde', 'link', 'lipsy', 'live', 'living', 'lixil', 'lk', 'loan', 'loans', 'locker', 'locus', 'loft', 'lol', 'london', 'lotte', 'lotto', 'love', 'lpl', 'lplfinancial', 'lr', 'ls', 'lt', 'ltd', 'ltda', 'lu', 'lundbeck', 'lupin', 'luxe', 'luxury', 'lv', 'ly', 'ma', 'macys', 'madrid', 'maif', 'maison', 'makeup', 'man', 'management', 'mango', 'map', 'market', 'marketing', 'markets', 'marriott', 'marshalls', 'maserati', 'mattel', 'mba', 'mc', 'mckinsey', 'md', 'me', 'med', 'media', 'meet', 'melbourne', 'meme', 'memorial', 'men', 'menu', 'meo', 'merckmsd', 'metlife', 'mg', 'mh', 'miami', 'microsoft', 'mil', 'mini', 'mint', 'mit', 'mitsubishi', 'mk', 'ml', 'mlb', 'mls', 'mm', 'mma', 'mn', 'mo', 'mobi', 'mobile', 'mobily', 'moda', 'moe', 'moi', 'mom', 'monash', 'money', 'monster', 'mopar', 'mormon', 'mortgage', 'moscow', 'moto', 'motorcycles', 'mov', 'movie', 'movistar', 'mp', 'mq', 'mr', 'ms', 'msd', 'mt', 'mtn', 'mtr', 'mu', 'museum', 'mutual', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'nab', 'nadex', 'nagoya', 'name', 'nationwide', 'natura', 'navy', 'nba', 'nc', 'ne', 'nec', 'net', 'netbank', 'netflix', 'network', 'neustar', 'new', 'newholland', 'news', 'next', 'nextdirect', 'nexus', 'nf', 'nfl', 'ng', 'ngo', 'nhk', 'ni', 'nico', 'nike', 'nikon', 'ninja', 'nissan', 'nissay', 'nl', 'no', 'nokia', 'northwesternmutual', 'norton', 'now', 'nowruz', 'nowtv', 'np', 'nr', 'nra', 'nrw', 'ntt', 'nu', 'nyc', 'nz', 'obi', 'observer', 'off', 'office', 'okinawa', 'olayan', 'olayangroup', 'oldnavy', 'ollo', 'om', 'omega', 'one', 'ong', 'onl', 'online', 'onyourside', 'ooo', 'open', 'oracle', 'orange', 'org', 'organic', 'origins', 'osaka', 'otsuka', 'ott', 'ovh', 'pa', 'page', 'panasonic', 'panerai', 'paris', 'pars', 'partners', 'parts', 'party', 'passagens', 'pay', 'pccw', 'pe', 'pet', 'pf', 'pfizer', 'pg', 'ph', 'pharmacy', 'phd', 'philips', 'phone', 'photo', 'photography', 'photos', 'physio', 'piaget', 'pics', 'pictet', 'pictures', 'pid', 'pin', 'ping', 'pink', 'pioneer', 'pizza', 'pk', 'pl', 'place', 'play', 'playstation', 'plumbing', 'plus', 'pm', 'pn', 'pnc', 'pohl', 'poker', 'politie', 'porn', 'post', 'pr', 'pramerica', 'praxi', 'press', 'prime', 'pro', 'prod', 'productions', 'prof', 'progressive', 'promo', 'properties', 'property', 'protection', 'pru', 'prudential', 'ps', 'pt', 'pub', 'pw', 'pwc', 'py', 'qa', 'qpon', 'quebec', 'quest', 'qvc', 'racing', 'radio', 'raid', 're', 'read', 'realestate', 'realtor', 'realty', 'recipes', 'red', 'redstone', 'redumbrella', 'rehab', 'reise', 'reisen', 'reit', 'reliance', 'ren', 'rent', 'rentals', 'repair', 'report', 'republican', 'rest', 'restaurant', 'review', 'reviews', 'rexroth', 'rich', 'richardli', 'ricoh', 'rightathome', 'ril', 'rio', 'rip', 'rmit', 'ro', 'rocher', 'rocks', 'rodeo', 'rogers', 'room', 'rs', 'rsvp', 'ru', 'rugby', 'ruhr', 'run', 'rw', 'rwe', 'ryukyu', 'sa', 'saarland', 'safe', 'safety', 'sakura', 'sale', 'salon', 'samsclub', 'samsung', 'sandvik', 'sandvikcoromant', 'sanofi', 'sap', 'sapo', 'sarl', 'sas', 'save', 'saxo', 'sb', 'sbi', 'sbs', 'sc', 'sca', 'scb', 'schaeffler', 'schmidt', 'scholarships', 'school', 'schule', 'schwarz', 'science', 'scjohnson', 'scor', 'scot', 'sd', 'se', 'search', 'seat', 'secure', 'security', 'seek', 'select', 'sener', 'services', 'ses', 'seven', 'sew', 'sex', 'sexy', 'sfr', 'sg', 'sh', 'shangrila', 'sharp', 'shaw', 'shell', 'shia', 'shiksha', 'shoes', 'shop', 'shopping', 'shouji', 'show', 'showtime', 'shriram', 'si', 'silk', 'sina', 'singles', 'site', 'sj', 'sk', 'ski', 'skin', 'sky', 'skype', 'sl', 'sling', 'sm', 'smart', 'smile', 'sn', 'sncf', 'so', 'soccer', 'social', 'softbank', 'software', 'sohu', 'solar', 'solutions', 'song', 'sony', 'soy', 'space', 'spiegel', 'spot', 'spreadbetting', 'sr', 'srl', 'srt', 'st', 'stada', 'staples', 'star', 'starhub', 'statebank', 'statefarm', 'statoil', 'stc', 'stcgroup', 'stockholm', 'storage', 'store', 'stream', 'studio', 'study', 'style', 'su', 'sucks', 'supplies', 'supply', 'support', 'surf', 'surgery', 'suzuki', 'sv', 'swatch', 'swiftcover', 'swiss', 'sx', 'sy', 'sydney', 'symantec', 'systems', 'sz', 'tab', 'taipei', 'talk', 'taobao', 'target', 'tatamotors', 'tatar', 'tattoo', 'tax', 'taxi', 'tc', 'tci', 'td', 'tdk', 'team', 'tech', 'technology', 'tel', 'telecity', 'telefonica', 'temasek', 'tennis', 'teva', 'tf', 'tg', 'th', 'thd', 'theater', 'theatre', 'tiaa', 'tickets', 'tienda', 'tiffany', 'tips', 'tires', 'tirol', 'tj', 'tjmaxx', 'tjx', 'tk', 'tkmaxx', 'tl', 'tm', 'tmall', 'tn', 'to', 'today', 'tokyo', 'tools', 'top', 'toray', 'toshiba', 'total', 'tours', 'town', 'toyota', 'toys', 'tr', 'trade', 'trading', 'training', 'travel', 'travelchannel', 'travelers', 'travelersinsurance', 'trust', 'trv', 'tt', 'tube', 'tui', 'tunes', 'tushu', 'tv', 'tvs', 'tw', 'tz', 'ua', 'ubank', 'ubs', 'uconnect', 'ug', 'uk', 'unicom', 'university', 'uno', 'uol', 'ups', 'us', 'uy', 'uz', 'va', 'vacations', 'vana', 'vanguard', 'vc', 've', 'vegas', 'ventures', 'verisign', 'versicherung', 'vet', 'vg', 'vi', 'viajes', 'video', 'vig', 'viking', 'villas', 'vin', 'vip', 'virgin', 'visa', 'vision', 'vista', 'vistaprint', 'viva', 'vivo', 'vlaanderen', 'vn', 'vodka', 'volkswagen', 'volvo', 'vote', 'voting', 'voto', 'voyage', 'vu', 'vuelos', 'wales', 'walmart', 'walter', 'wang', 'wanggou', 'warman', 'watch', 'watches', 'weather', 'weatherchannel', 'webcam', 'weber', 'website', 'wed', 'wedding', 'weibo', 'weir', 'wf', 'whoswho', 'wien', 'wiki', 'williamhill', 'win', 'windows', 'wine', 'winners', 'wme', 'wolterskluwer', 'woodside', 'work', 'works', 'world', 'wow', 'ws', 'wtc', 'wtf', 'xbox', 'xerox', 'xfinity', 'xihuan', 'xin', 'xn--11b4c3d', 'xn--1ck2e1b', 'xn--1qqw23a', 'xn--2scrj9c', 'xn--30rr7y', 'xn--3bst00m', 'xn--3ds443g', 'xn--3e0b707e', 'xn--3hcrj9c', 'xn--3oq18vl8pn36a', 'xn--3pxu8k', 'xn--42c2d9a', 'xn--45br5cyl', 'xn--45brj9c', 'xn--45q11c', 'xn--4gbrim', 'xn--54b7fta0cc', 'xn--55qw42g', 'xn--55qx5d', 'xn--5su34j936bgsg', 'xn--5tzm5g', 'xn--6frz82g', 'xn--6qq986b3xl', 'xn--80adxhks', 'xn--80ao21a', 'xn--80aqecdr1a', 'xn--80asehdb', 'xn--80aswg', 'xn--8y0a063a', 'xn--90a3ac', 'xn--90ae', 'xn--90ais', 'xn--9dbq2a', 'xn--9et52u', 'xn--9krt00a', 'xn--b4w605ferd', 'xn--bck1b9a5dre4c', 'xn--c1avg', 'xn--c2br7g', 'xn--cck2b3b', 'xn--cg4bki', 'xn--clchc0ea0b2g2a9gcd', 'xn--czr694b', 'xn--czrs0t', 'xn--czru2d', 'xn--d1acj3b', 'xn--d1alf', 'xn--e1a4c', 'xn--eckvdtc9d', 'xn--efvy88h', 'xn--estv75g', 'xn--fct429k', 'xn--fhbei', 'xn--fiq228c5hs', 'xn--fiq64b', 'xn--fiqs8s', 'xn--fiqz9s', 'xn--fjq720a', 'xn--flw351e', 'xn--fpcrj9c3d', 'xn--fzc2c9e2c', 'xn--fzys8d69uvgm', 'xn--g2xx48c', 'xn--gckr3f0f', 'xn--gecrj9c', 'xn--gk3at1e', 'xn--h2breg3eve', 'xn--h2brj9c', 'xn--h2brj9c8c', 'xn--hxt814e', 'xn--i1b6b1a6a2e', 'xn--imr513n', 'xn--io0a7i', 'xn--j1aef', 'xn--j1amh', 'xn--j6w193g', 'xn--jlq61u9w7b', 'xn--jvr189m', 'xn--kcrx77d1x4a', 'xn--kprw13d', 'xn--kpry57d', 'xn--kpu716f', 'xn--kput3i', 'xn--l1acc', 'xn--lgbbat1ad8j', 'xn--mgb9awbf', 'xn--mgba3a3ejt', 'xn--mgba3a4f16a', 'xn--mgba7c0bbn0a', 'xn--mgbaakc7dvf', 'xn--mgbaam7a8h', 'xn--mgbab2bd', 'xn--mgbai9azgqp6j', 'xn--mgbayh7gpa', 'xn--mgbb9fbpob', 'xn--mgbbh1a', 'xn--mgbbh1a71e', 'xn--mgbc0a9azcg', 'xn--mgbca7dzdo', 'xn--mgberp4a5d4ar', 'xn--mgbgu82a', 'xn--mgbi4ecexp', 'xn--mgbpl2fh', 'xn--mgbt3dhd', 'xn--mgbtx2b', 'xn--mgbx4cd0ab', 'xn--mix891f', 'xn--mk1bu44c', 'xn--mxtq1m', 'xn--ngbc5azd', 'xn--ngbe9e0a', 'xn--ngbrx', 'xn--node', 'xn--nqv7f', 'xn--nqv7fs00ema', 'xn--nyqy26a', 'xn--o3cw4h', 'xn--ogbpf8fl', 'xn--p1acf', 'xn--p1ai', 'xn--pbt977c', 'xn--pgbs0dh', 'xn--pssy2u', 'xn--q9jyb4c', 'xn--qcka1pmc', 'xn--qxam', 'xn--rhqv96g', 'xn--rovu88b', 'xn--rvc1e0am3e', 'xn--s9brj9c', 'xn--ses554g', 'xn--t60b56a', 'xn--tckwe', 'xn--tiq49xqyj', 'xn--unup4y', 'xn--vermgensberater-ctb', 'xn--vermgensberatung-pwb', 'xn--vhquv', 'xn--vuq861b', 'xn--w4r85el8fhu5dnra', 'xn--w4rs40l', 'xn--wgbh1c', 'xn--wgbl6a', 'xn--xhq521b', 'xn--xkc2al3hye2a', 'xn--xkc2dl3a5ee0h', 'xn--y9a3aq', 'xn--yfro4i67o', 'xn--ygbi2ammx', 'xn--zfr164b', 'xperia', 'xxx', 'xyz', 'yachts', 'yahoo', 'yamaxun', 'yandex', 'ye', 'yodobashi', 'yoga', 'yokohama', 'you', 'youtube', 'yt', 'yun', 'za', 'zappos', 'zara', 'zero', 'zip', 'zippo', 'zm', 'zone', 'zuerich', 'zw']

_SCHEME = r'(?:http|https|file|irc):/{1,3}'
_HOST = r'(?:[a-z0-9][a-z0-9\-]*\.)+(?:' + '|'.join(TLDS) + r')(?::\d{2,6})?'
_PATH = r'/[\w/.\-_~.;:%?!@$#&()=+]*'

LINKIFY_RE = re.compile(r'(?:{scheme})?{host}(?:{path}|\b)'
                        .format(scheme=_SCHEME, host=_HOST, path=_PATH),
                        re.VERBOSE | re.UNICODE | re.IGNORECASE)

FORMAT_NOTE = 'note'
FORMAT_ARTICLE = 'article'

DELIMITERS = ',.;: \t\r\n'

# Based on
# https://en.m.wikipedia.org/wiki/Category:Writing_systems_without_word_boundaries
# https://en.m.wikipedia.org/wiki/List_of_ISO_639_language_codes
NON_WORD_DELIMITED_LANGS = ('ja', 'zh', 'th', 'vi', 'my', 'km', 'lo')

# From https://developer.twitter.com/en/docs/developer-utilities/twitter-text
# on 2017-11-18.
WEIGHTS = {
    'version': 2,
    'maxWeightedTweetLength': 280,
    'scale': 100,
    'defaultWeight': 200,
    'transformedURLLength': 23,
    'ranges': [
        {'start': 0, 'end': 4351, 'weight': 100},
        {'start': 8192, 'end': 8205, 'weight': 100},
        {'start': 8208, 'end': 8223, 'weight': 100},
        {'start': 8242, 'end': 8247, 'weight': 100},
    ],
}


class Token:
    def __init__(self, tag, content, required=False):
        self.tag = tag
        self.content = content
        self.required = required

    def __eq__(self, o):
        return self.tag == o.tag \
            and self.content == o.content \
            and self.required == o.required

    def __repr__(self):
        return u'Token(tag={}, content={}, required={})'.format(
            self.tag, self.content, self.required)


def tokenize(text):
    """Split text into link and non-link text, a list of brevity.Tokens,
    tagged with 'text' or 'link' depending on how they should be
    interpreted.

    :param string text: text to tokenize

    :return list: a list of brevity.Tokens
    """
    links = LINKIFY_RE.findall(text)
    splits = LINKIFY_RE.split(text)

    for ii in xrange(len(links)):
        # trim trailing punctuation from links
        link = links[ii]
        jj = len(link) - 1
        while (jj >= 0 and link[jj] in '.!?,;:)'
               # allow 1 () pair
               and (link[jj] != ')' or '(' not in link)):
            jj -= 1
            links[ii] = link[:jj + 1]
            splits[ii + 1] = link[jj + 1:] + splits[ii + 1]
            link = links[ii]

        # avoid double linking by looking at preceeding 2 chars
        prev_text = splits[ii]
        next_text = splits[ii + 1]
        if (prev_text.rstrip().endswith('="')
                or prev_text.rstrip().endswith("='")
                or prev_text.endswith('@') or next_text.startswith('@')
                or prev_text.endswith('$') or prev_text.endswith('/')
                or prev_text.endswith('.') or prev_text.endswith('#')
                or prev_text.endswith('_') or prev_text.endswith('-')
                or next_text.lstrip().startswith('</a')):
            # collapse link into before text
            splits[ii] = splits[ii] + links[ii]
            links[ii] = None
            continue

    # compile the tagged tokens
    result = []
    for ii in xrange(max(len(links), len(splits))):
        if ii < len(splits) and splits[ii]:
            if result and result[-1].tag == 'text':
                # collapse consecutive text tokens
                result[-1].content += splits[ii]
            else:
                result.append(Token('text', splits[ii]))
        if ii < len(links) and links[ii]:
            result.append(Token('link', links[ii]))

    return result


def autolink(text):
    """Add <a> tags around web addresses in an HTML or plain text
    document. URLs inside pre-existing HTML elements will be left alone.

    :param string text: the text document with addresses to mark up
    :return string: the text with addresses replaced by <a> elements
    """
    def add_scheme(url):
        if (url.startswith('//') or url.startswith('http://')
                or url.startswith('https://') or url.startswith('mailto://')
                or url.startswith('irc://')):
            return url
        if url.startswith('Http://') or url.startswith('Https://'):
            return 'h' + url[1:]
        return 'http://' + url

    result = []
    for token in tokenize(text):
        if token.tag == 'link':
            result.append('<a class="auto-link" href="{0}">{1}</a>'.format(
                add_scheme(token.content), token.content))
        else:
            result.append(token.content)
    return ''.join(result)


def shorten(text, permalink=None, permashortlink=None, permashortcitation=None,
            target_length=WEIGHTS['maxWeightedTweetLength'],
            link_length=WEIGHTS['transformedURLLength'],
            format=FORMAT_NOTE, ellipsis=u'…', punctuation=(' (', ')'), weights=True,
            lang=None):
    """Prepare note text for publishing as a tweet. Ellipsize and add a
    permalink or citation.

    If the full text plus optional '(permashortlink)' or
    '(permashortcitation)' can fit into the target length (defaults to
    280 characters), it will return the composed text.

    If format is FORMAT_ARTICLE, text is taken to be the title of a longer
    article. It will be formatted as '[text]: [permalink]'. The values of
    permashortlink and permashortcitation are ignored in this case.

    Otherwise, the text will be shortened to the nearest full word,
    with an ellipsis and permalink added at the end. A permalink
    should always be provided; otherwise text will be shortened with
    no way to find the original.

    Note: that the permashortlink does not actually have to be a
    "short" URL. It is totally reasonable to provide the same URL for
    both the permalink and permashortlink.

    :param string text: The full note text that may be ellipsized
    :param string permalink: URL of the original note, will only be added if
      the text is shortened (optional).
    :param string permashortlink: Short URL of the original note, if provided
      will be added to the end of all notes. (optional)
    :param string permashortcitation: Citation to the original note, e.g.
      'ttk.me t4_f2', an alternative to permashortlink. If provided will be
      added to the end of all notes. (optional)
    :param int target_length: The target overall length (default = 280)
    :param int link_length: The t.co length for a URL. If 'None', URLs won't be special cased and will count like normal characters. (default = 23)
    :param string format: one of the FORMAT_ constants that determines
      whether to format the text like a note or an article (default = FORMAT_NOTE)
    :param string ellipsis: The string to append to text when it's truncated (default = '…')
    :param tuple(string, string) punctuation: The prefix and suffix strings to enclose the permalink, permashortlink, or permashortcitation with (default = (' (', ')'))
    :param bool weights: Whether to use Twitter's weights when counting characters. (default = True)
    :param string lang: optional ISO 639-1 two-character language code for the
      content's language. If it's in 'NON_WORD_DELIMITED_LANGS', truncation will
      happen exactly at 'target_length', and whitespace will be ignored. (optional)

    :return string: the final composed text
    """
    def truncate_to_nearest_word(text, length):
        # try stripping trailing whitespace first
        text = text.rstrip()
        if str_length(text) <= length:
            return text
        # walk backwards until we find a delimiter
        for j in xrange(len(text) - 1, -1, -1):
            if text[j] in DELIMITERS or lang in NON_WORD_DELIMITED_LANGS:
                trunc = text[:j].rstrip(DELIMITERS)
                if str_length(trunc) <= length:
                    return trunc
        # walk backwards ignoring delimiters
        for j in xrange(len(text) - 1, -1, -1):
            trunc = text[:j]
            if str_length(trunc) <= length:
                return trunc
        warnings.warn('Failed to truncate text "{}" to {} characters. This indicates a logical error'.format(text, length))
        return ''

    def char_length(char):
        if not weights:
            return 1

        point = ord(char)
        weight = WEIGHTS['defaultWeight']
        for range in WEIGHTS['ranges']:
            if point >= range['start'] and point <= range['end']:
                weight = range['weight']
        return weight // WEIGHTS['scale']

    def str_length(val):
        return sum(char_length(char) for char in val)

    def token_length(token):
        if token.tag == 'link' and link_length is not None:
            return link_length
        return str_length(token.content)

    def total_length(tokens):
        return sum(token_length(t) for t in tokens)

    tokens = tokenize(text)

    citation_tokens = []
    if FORMAT_ARTICLE in format and permalink:
        citation_tokens.append(Token('text', ': ', True))
        citation_tokens.append(Token('link', permalink, True))
    elif permashortlink:
        citation_tokens.append(Token('text', punctuation[0], True))
        citation_tokens.append(Token('link', permashortlink, True))
        citation_tokens.append(Token('text', punctuation[1], True))
    elif permashortcitation:
        citation_tokens.append(
            Token('text', punctuation[0] + permashortcitation + punctuation[1], True))

    if 'media' in format:
        print('Brevity: "media" formatting has been removed; Media attachments no longer count against Twitter\'s character limit (https://dev.twitter.com/overview/api/upcoming-changes-to-tweets)', file=sys.stderr)

    base_length = total_length(tokens)
    citation_length = total_length(citation_tokens)

    if base_length + citation_length <= target_length:
        tokens += citation_tokens

    else:
        # add permalink
        if permalink:
            tokens.append(Token('text', ellipsis + ' ', True))
            tokens.append(Token('link', permalink, True))
        else:
            tokens.append(Token('text', ellipsis, True))

        # drop or shorten tokens, starting from the end
        for ii in xrange(len(tokens) - 1, -1, -1):
            token = tokens[ii]
            if token.required:
                continue

            over = total_length(tokens) - target_length
            if over <= 0:
                # strip trailing whitespace and punctuation on the last token
                if token.tag == 'text':
                    token.content = token.content.rstrip(DELIMITERS)
                break

            if token.tag == 'link':
                del tokens[ii]
            elif token.tag == 'text':
                toklen = token_length(token)
                if over >= toklen:
                    del tokens[ii]
                else:
                    token.content = truncate_to_nearest_word(
                        token.content, toklen - over)

    return ''.join(t.content for t in tokens)
