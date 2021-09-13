ordered_symbols = ["USDC", "WALGO", "YLDY", "BANK"]
assets = {
            "USDC": 26553902, 
            "WALGO": 26553903, 
            "YLDY": 26553905, 
            "BANK": 26553906,
            "bUSDC": 26554530, 
            "bWALGO": 26554561, 
            "bYLDY": 26554605, 
            "bBANK": 26554643
        }

escrow_hashes = {
                    "USDC": "FHR2FO5D5GPLAZVGYIC2ZHNLUYOG2PZWQB6NVIZWBHJO76V7CZWUBM4CXQ", 
                    "WALGO": "WTRVTZK5S2COIAJRMPMHEVX6ZQHYKTVQ3PB3CEB7DRZOML5WIN24NOBSDY",
                    "YLDY": "RUVXATVPJ7346EZXABEZPXNH3YOMGQLQRIIDABW37LM66AFAQU3NT44J3M", 
                    "BANK": "AO3XAUOVJ32A5PNVEUL435CFTFHWIX6SP67YM23P7UWNZNWLNILTSVHPRI"
                }

escrow_programs = {
                    "USDC": "BCAFAQYA0d/UDAgzAQAzAAASRDMCADMAABJEMwMAMwAAEkQzBAAzAAASRDEWIxJEMwAQIxIzABglEhAzABkkEhAzARAjEhAzARglEhAzARkkEhAzAhAjEhAzAhglEhAzAhkkEhAzAxAjEhAzAxglEhAzAxkkEhAzBBAjEhAzBBglEhAzBBkkEhAzBRAjEhAzBRiB0t/UDBIQMwUZJBIQMgQhBBJAAdoiEEQxIDIDEkQyBCEEEjcEGgCACWxpcXVpZGF0ZRIQQAGoMgSBBxJAAAEANwQaAIAYY3JlYXRlX2xpbmtlZF9iYW5rX2Fzc2V0EkAAzTcEGgCABm9wdF9pbhJAAL03BBoAgARtaW50EkAArzcEGgCACmNsYWltX21pbnQSQACbNwQaAIAEYnVybhJAAI03BBoAgApjbGFpbV9idXJuEkAAeTcEGgCADmFkZF9jb2xsYXRlcmFsEkAAYTcEGgCAEXJlbW92ZV9jb2xsYXRlcmFsEkAARjcEGgCADGNsYWltX2JvcnJvdxJAADA3BBoAgAxyZXBheV9ib3Jyb3cSQAAaNwQaAIAPY2xhaW1fbGlxdWlkYXRlEkAAAQAxEzIDEkQxFTIDEkQiQgC+MRMyAxJEMRUyAxJEIkL/7TETMgMSRDEVMgMSRCJC/90xEzIDEkQxFTIDEkQiQv/NMRMyAxJEMRUyAxJEIkL/vTETMgMSRDEVMgMSRCJC/60xEzIDEkQxFTIDEkQiQv+dMRMyAxJEMRUyAxJEIkL/jTETMgMSRDEVMgMSRCJC/30xEzIDEkQxFTIDEkQiQv9tMRMyAxJEMRUyAxJEIkL/XTETMgMSRDEVMgMSRCJCAA4zBxAjEjMHGSQSEEL+GQ==",
                    "WALGO": "BCAFAQYA0d/UDAgzAQAzAAASRDMCADMAABJEMwMAMwAAEkQzBAAzAAASRDEWIxJEMwAQIxIzABglEhAzABkkEhAzARAjEhAzARglEhAzARkkEhAzAhAjEhAzAhglEhAzAhkkEhAzAxAjEhAzAxglEhAzAxkkEhAzBBAjEhAzBBglEhAzBBkkEhAzBRAjEhAzBRiB09/UDBIQMwUZJBIQMgQhBBJAAdoiEEQxIDIDEkQyBCEEEjcEGgCACWxpcXVpZGF0ZRIQQAGoMgSBBxJAAAEANwQaAIAYY3JlYXRlX2xpbmtlZF9iYW5rX2Fzc2V0EkAAzTcEGgCABm9wdF9pbhJAAL03BBoAgARtaW50EkAArzcEGgCACmNsYWltX21pbnQSQACbNwQaAIAEYnVybhJAAI03BBoAgApjbGFpbV9idXJuEkAAeTcEGgCADmFkZF9jb2xsYXRlcmFsEkAAYTcEGgCAEXJlbW92ZV9jb2xsYXRlcmFsEkAARjcEGgCADGNsYWltX2JvcnJvdxJAADA3BBoAgAxyZXBheV9ib3Jyb3cSQAAaNwQaAIAPY2xhaW1fbGlxdWlkYXRlEkAAAQAxEzIDEkQxFTIDEkQiQgC+MRMyAxJEMRUyAxJEIkL/7TETMgMSRDEVMgMSRCJC/90xEzIDEkQxFTIDEkQiQv/NMRMyAxJEMRUyAxJEIkL/vTETMgMSRDEVMgMSRCJC/60xEzIDEkQxFTIDEkQiQv+dMRMyAxJEMRUyAxJEIkL/jTETMgMSRDEVMgMSRCJC/30xEzIDEkQxFTIDEkQiQv9tMRMyAxJEMRUyAxJEIkL/XTETMgMSRDEVMgMSRCJCAA4zBxAjEjMHGSQSEEL+GQ==",
                    "YLDY": "BCAFAQYA0d/UDAgzAQAzAAASRDMCADMAABJEMwMAMwAAEkQzBAAzAAASRDEWIxJEMwAQIxIzABglEhAzABkkEhAzARAjEhAzARglEhAzARkkEhAzAhAjEhAzAhglEhAzAhkkEhAzAxAjEhAzAxglEhAzAxkkEhAzBBAjEhAzBBglEhAzBBkkEhAzBRAjEhAzBRiB1d/UDBIQMwUZJBIQMgQhBBJAAdoiEEQxIDIDEkQyBCEEEjcEGgCACWxpcXVpZGF0ZRIQQAGoMgSBBxJAAAEANwQaAIAYY3JlYXRlX2xpbmtlZF9iYW5rX2Fzc2V0EkAAzTcEGgCABm9wdF9pbhJAAL03BBoAgARtaW50EkAArzcEGgCACmNsYWltX21pbnQSQACbNwQaAIAEYnVybhJAAI03BBoAgApjbGFpbV9idXJuEkAAeTcEGgCADmFkZF9jb2xsYXRlcmFsEkAAYTcEGgCAEXJlbW92ZV9jb2xsYXRlcmFsEkAARjcEGgCADGNsYWltX2JvcnJvdxJAADA3BBoAgAxyZXBheV9ib3Jyb3cSQAAaNwQaAIAPY2xhaW1fbGlxdWlkYXRlEkAAAQAxEzIDEkQxFTIDEkQiQgC+MRMyAxJEMRUyAxJEIkL/7TETMgMSRDEVMgMSRCJC/90xEzIDEkQxFTIDEkQiQv/NMRMyAxJEMRUyAxJEIkL/vTETMgMSRDEVMgMSRCJC/60xEzIDEkQxFTIDEkQiQv+dMRMyAxJEMRUyAxJEIkL/jTETMgMSRDEVMgMSRCJC/30xEzIDEkQxFTIDEkQiQv9tMRMyAxJEMRUyAxJEIkL/XTETMgMSRDEVMgMSRCJCAA4zBxAjEjMHGSQSEEL+GQ==",
                    "BANK": "BCAFAQYA0d/UDAgzAQAzAAASRDMCADMAABJEMwMAMwAAEkQzBAAzAAASRDEWIxJEMwAQIxIzABglEhAzABkkEhAzARAjEhAzARglEhAzARkkEhAzAhAjEhAzAhglEhAzAhkkEhAzAxAjEhAzAxglEhAzAxkkEhAzBBAjEhAzBBglEhAzBBkkEhAzBRAjEhAzBRiB1t/UDBIQMwUZJBIQMgQhBBJAAdoiEEQxIDIDEkQyBCEEEjcEGgCACWxpcXVpZGF0ZRIQQAGoMgSBBxJAAAEANwQaAIAYY3JlYXRlX2xpbmtlZF9iYW5rX2Fzc2V0EkAAzTcEGgCABm9wdF9pbhJAAL03BBoAgARtaW50EkAArzcEGgCACmNsYWltX21pbnQSQACbNwQaAIAEYnVybhJAAI03BBoAgApjbGFpbV9idXJuEkAAeTcEGgCADmFkZF9jb2xsYXRlcmFsEkAAYTcEGgCAEXJlbW92ZV9jb2xsYXRlcmFsEkAARjcEGgCADGNsYWltX2JvcnJvdxJAADA3BBoAgAxyZXBheV9ib3Jyb3cSQAAaNwQaAIAPY2xhaW1fbGlxdWlkYXRlEkAAAQAxEzIDEkQxFTIDEkQiQgC+MRMyAxJEMRUyAxJEIkL/7TETMgMSRDEVMgMSRCJC/90xEzIDEkQxFTIDEkQiQv/NMRMyAxJEMRUyAxJEIkL/vTETMgMSRDEVMgMSRCJC/60xEzIDEkQxFTIDEkQiQv+dMRMyAxJEMRUyAxJEIkL/jTETMgMSRDEVMgMSRCJC/30xEzIDEkQxFTIDEkQiQv9tMRMyAxJEMRUyAxJEIkL/XTETMgMSRDEVMgMSRCJCAA4zBxAjEjMHGSQSEEL+GQ=="
                }

manager_id = "26554321"
storage_ids = {
                "USDC": 26554322, 
                "WALGO": 26554323, 
                "YLDY": 26554325, 
                "BANK": 26554326
            }
oracle_ids = {
            "USDC": 26554334, 
            "WALGO": 26554336, 
            "YLDY": 26554337, 
            "BANK": 26554338
            }