'''
Defines an interface for method chaining to build up an object to scrape auto-
motive listings from craigslist.
'''


class CL_URL(object):
    '''Progressively build valid automotive search URL keyword arguments.
    
    Craiglist uses its own mapping of url keyword to url parameter to build a
    search query.
    '''
    def __init__(
        self,
        query=None,
        cities=None, 
        include_nearby=False,
        miles_from_zip=None,
        zipcode=None,
        price_range=(None, None),
        model_year_range=(None, None),
        odo_range=(None, None),
        condition_codes=None,
        cylinders=None,
        drive_types=None,
        fuel_types=None,
        paint_colors=None,
        size_types=None,
        title_statuses=None,
        transmission_types=None,
        vehicle_types=None,
    ):
        """These are the available parameters that can be supplied as parameters
        to the craigslist URL.

        There are a few different 'kinds' of parameters supplied to the url
        parameter list. Although all URL parameters are ultimately mapped down
        to keywords, we can abstract this complexity away into lists.
        
        """

        self._SEARCH_NEARBY = 'searchNearby'
        def process_param(param):
            '''Returns param if it isn't a list'''

            print(param, type(param))
            if param is None:
                return param
            if isinstance(param, str):
                return [param]
            return list(param)

        self._url_template = "https://{city}.craigslist.org/search/cta"
        self._query = process_param(query)
        self._cities = process_param(cities)
        self._condition_codes = process_param(condition_codes)
        self._cylinders = process_param(cylinders)
        self._drive_types = process_param(drive_types)
        self._fuel_types = process_param(fuel_types)
        self._paint_colors = process_param(paint_colors)
        self._size_types = process_param(size_types)
        self._title_statuses = process_param(title_statuses)
        self._transmission_types = process_param(transmission_types)
        self._vehicle_types = process_param(vehicle_types)

        self._city_urls = []
        for city in self._cities:
            self._city_urls.append(self._url_template.format(city=city))

        print(self._city_urls)

        self._url_params = []

        return self


    def include_nearby():
        self._url_params = [ (key, val) for key, val in self._url_params if key != _SEARCH_NEARBY ]



class AutoScraper(object):
    def __init__(
        self,
        url,
        make,
        model,
        year,
        price_min,
        price_max,
    ):
        print("IMPLEMENT ME")

