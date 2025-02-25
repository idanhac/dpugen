#!/usr/bin/python3

import sys

from confbase import ConfBase
from confutils import common_main


class VpcMappingTypes(ConfBase):

    def __init__(self, params={}):
        super().__init__('vpc-mappings-routing-types', params)
        self.num_yields = 0

    def items(self):
        print('  Generating %s...' % self.dictname, file=sys.stderr)
        p = self.params
        cp = self.cooked_params

        vpcmappingtypes = [
            "vpc",
            "privatelink",
            "privatelinknsg"
        ]

        # return generator from list for consistency with other subgenerators
        for x in vpcmappingtypes:

            self.num_yields += 1
            yield x


if __name__ == "__main__":
    conf = VpcMappingTypes()
    common_main(conf)
