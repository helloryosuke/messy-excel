#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# messy_excel: Split Pandas read_excel results into multiple dataframes
# https://github.com/helloryosuke/japan-real-estate-data
#
# Copyright 2021-2022 Ryosuke Inaba
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import pandas as _pd

class MessyExcel:
    
    def __init__(self, io, sheet_name=0):
        """
        Cleans messy excel files by splitting the dataframe resulting from pandas' read_excel functionality into multiple

        Parameters:
        ------------
            io: (taken from pandas documentation) Any valid string path is acceptable. The string could be a URL. 
            Valid URL schemes include http, ftp, s3, and file. For file URLs, a host is expected. 
            A local file could be: file://localhost/path/to/table.xlsx. If you want to pass in a path object, pandas accepts any os.PathLike.
            By file-like object, we refer to objects with a read() method, such as a file handle (e.g. via builtin open function) or StringIO.
        """
        self._df:_pd.DataFrame = _pd.read_excel(io, sheet_name=sheet_name) # raw dataframe object
        self._master:list = [] # resulting list of DataFrames
        self._process() # execute process
        
    def _process(self):
        """split resulting dataframe of pandas read_excel functionality by splitting by extra spaces"""

        try:
            # initialize first column
            na_cols:list = [-1]

            # iterate over columns to find na cols
            for i, (col_name, col) in enumerate(self._df.items()):    
                if len(col.dropna())==0:
                    na_cols.append(i)

            # add extra col to iterate over
            na_cols.append(None)
            
            # save split-by-cols data
            col_data:list = []

            # iterate over columns
            for i, col in enumerate(na_cols):

                # if column is note a None (extra columns index)
                if col!=None:
                    left = col + 1 # set start left col index
                    right = na_cols[i+1] # set ending right col index

                    # if right index is an extra col index
                    if right==None:
                        d = self._df.iloc[:,left:].copy() # loc all columns beyond left col
                    else:
                        d = self._df.iloc[:,left:right].copy() # loc all columns between right and left col

                    # if the resulting dataframe contains data
                    if d.size > 0:
                        col_data.append(d) # append to col_data list
                        
            master:list = []

            # iterate over the dataframes split by columns
            for data in col_data:

                # initialize beginning row index
                na_rows = [-1]

                # iterate over rows
                for i, (row_name, row) in enumerate(data.iterrows()):  
                    
                    # find nan rows
                    if len(row.dropna())==0:
                        na_rows.append(i)

                # add extra row index
                na_rows.append(None)

                # save resulting rows
                rows_data:list = []

                # iterate over rows
                for i, row in enumerate(na_rows):

                    # if the row index is not a None (extra row index)
                    if row!=None:
                        top = row + 1 # set top row index
                        bottom = na_rows[i+1] # set bottom row index

                        # if the bottom row index is a None
                        if bottom==None:
                            d = data.iloc[top:,:] # trim all rows from top index row to rest
                        else:
                            d = data.iloc[top:bottom,:] # otherwise, trim rows between top and bottom index
                        
                        # if the resulting data is not empty
                        if d.size > 0:
                            rows_data.append(d.reset_index(drop=True)) # append to rows_data

                master.extend(rows_data) # finalize all data
                
            self._master = master # set master as attribute

        except Exception as e:
            print(e)
        
    @property
    def datalist(self) -> _pd.DataFrame:
        """access the resulting list of dataframes split by extra spaces"""
        return self._master

if __name__ == "__main__":
    pass