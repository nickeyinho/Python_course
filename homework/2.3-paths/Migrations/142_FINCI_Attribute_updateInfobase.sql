------------------------------------------------------------------------------------
---------------------------------------- FIN CI ---------------------------------
------------------------------------------------------------------------------------

------------------------------------------------------------------------------------
-- Uploading Mode -- FinCiSoftUpType
------------------------------------------------------------------------------------

UPDATE InfoBase 
	SET 
		type_search = 'listv',
		type_edit = 'listv',
		type_val = 'text',
		list_val = 'DIRECT;G-REMOTE;REPOSITORY'
	WHERE object_value = 'FinCiSoftUpType'
