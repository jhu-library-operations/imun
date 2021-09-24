import re

class Image(object):

    def __init__(self, reference=None):
        """ Interface for interacting with OCI images
        :param reference: The reference and tag of the image.
        Examples:
         - ghcr.io/derekbelrose/test:1
         - derekbelrose/test:1
         - registry.hub.docker.com/derekbelrose/test:1
         """
        self.reference = reference

    def process(self):
        (name, tag) = self.parse_reference(self.reference)
        (domain, port, path, name) = self.parse_name(name)

        (tag, digest) = self.parse_tag(tag)
        print(domain, port, path, name, tag, digest)
        
    def parse_reference(self, name_tag):
        """ Parses the standard OCI image url based on the logic in docker's reference.go file.
        https://github.com/moby/moby/blob/master/vendor/github.com/docker/distribution/reference/reference.go
        :param name_tag: The name and image of the tag in one of the acceptable formats
        """
        top_level_parse_re = re.compile("^(.+):(.+)$")

        results = top_level_parse_re.match(name_tag)
        if results:
            return(results.group(1), results.group(2))
        else:
            return (None,None)

    def parse_tag(self, tag):
        """ Parses the tag and returns the separated components such as the tag and digest if provided

        :param tag: The tag part of an OCI image reference. This follows the ':'.
        :return: A tuple of (tag, digest). Digest could be None. Tag will default to 'latest' instead of None.
        """
        
        mytag = "latest"
        mydigest = None

        regex = "([\w\d\.\-]+)@?([\w\d\.\-]*)$"

        regex_matched = re.match(regex, tag)
        mytag = regex_matched.group(1)
        mydigest = regex_matched.group(2)
        
        if regex_matched is None:
            mytag = "latest"

        return (mytag, mydigest)
        
    def parse_name(self, name):
        """ Parses the first have of the reference looking for the domain (if it exists) and the path to the name of the image in the reference
        :param name: name portion of an OCI complaint image reference (first part separated by the ':')
        :returns: A tuple of (domain, port, path, image_name)
        """
        domain_regex = None
        image_name = re.split('/', name)[-1]
        domain = None
        path = None
        port = None
        
        split_paths = re.split('/', name)[0:-1]
        if re.search('\.', split_paths[0]) or split_paths[0] == "localhost":
            domain = split_paths[0]

        if re.search(':', domain):
            split_domain = re.split(':', domain)
            domain = split_domain[0]
            port = split_domain[1]
            
        path = '/'.join(re.split('/', name)[1:-1])

        return(domain, port, path, image_name)
        
