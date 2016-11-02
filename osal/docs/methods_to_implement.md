# Methods to Implement

There are a lot of functions which we need to implement<sup>[citation needed]</sup>.  
This is currently incomplete but intended to be a comprehensive list of methods required by the OSAL API, sorted by their priority.  
This list is to be updated with information about work completed/to be done of each method.  Please update the priority of any methods you feel need updated.  A method should not be a member of more than one priority list.  

### Methods Required for Development
These are methods which will make development possible or significantly faster.  For this reason, they should be implemented as early as possible.  They may be methods with will be commonly called in most of the other code which we write, or they may be useful for other aspects of development and debugging.  They may be called for by the OSAL API or not.  

This is currently empty.  Update this with any methods which should be implemented early to enable development.  

### Methods Required to Successfully Load cFE

@others update this as necessary. We know that there are more methods which we need to add to this list.  This is in a tentative list of when they are called.  

- [ ] CFE_PSP_ProcessArgumentDefaults
- [ ] OS_printf
- [ ] OS_API_Init
- [ ] OS_ModuleTableInit
- [ ] OS_TimerAPIInit
- [ ] OS_TimespecToUsec
- [ ] OS_FS_Init
- [ ] CFE_PSP_ModuleInit
- [ ] CFE_PSP_InitProcessorReservedMemory
- [ ] CFE_PSP_InitCDS
- [ ] CFE_PSP_InitResetArea
- [ ] CFE_PSP_InitVolatileDiskMem
- [ ] CFE_PSP_InitUserReservedArea
- [ ] CFE_PSP_GetResetArea
- [ ] CFE_PSP_MemSet
- [ ] CFE_PSP_GetTime
- [ ] OS_GetLocalTime
- [ ] CFE_PSP_MemCpy
- [ ] CFE_PSP_GetTimerTicksPerSecond
- [ ] CFE_PSP_GetTimerLow32Rollover
- [ ] CFE_PSP_GetVolatileDiskMem
- [ ] OS_mkfs
- [ ] OS_mount
- [ ] CFE_PSP_AttachExceptions
- [ ] OS_MutSemCreate
- [ ] OS_InterruptSafeLock
- [ ] OS_InterruptSafeUnlock
- [ ] OS_FindCreator
- [ ] CFE_PSP_GetCDSSize
- [ ] CFE_PSP_ReadFromCDS
- [ ] CFE_PSP_WriteToCDS
- [ ] OS_MutSemTake
- [ ] OS_MutSemGive
- [ ] CFE_PSP_MemRead8
- [ ] OS_TaskCreate
- [ ] OS_PriorityRemap
- [ ] OS_ConvertToArrayIndex
- [ ] OS_TaskDelay
- [ ] OS_TaskRegister
- [ ] CFE_PSP_SetDefaultExceptionEnvironment
- [ ] OS_TaskGetId
- [ ] OS_QueueCreate
- [ ] CFE_PSP_GetSpacecraftId
- [ ] CFE_PSP_GetProcessorId
- [ ] CFE_PSP_GetCFETextSegmentInfo
- [ ] OS_BinSemCreate
- [ ] OS_BinSemTake
- [ ] OS_TimeBaseGetIdByName
- [ ] OS_open
- [ ] OS_check_name_length
- [ ] OS_TranslatePath
- [ ] OS_QueueGet
- [ ] OS_read
- [ ] OS_CompAbsDelayTime
- [ ] OS_ModuleLoad
- [ ] OS_SymbolLookup
- [ ] OS_TaskInstallDeleteHandler
- [ ] OS_close
- [ ] OS_QueuePut
- [ ] OS_IdleLoop
- [ ] OS_BinSemGive
- [ ] OS_HeapGetInfo

### Methods required by the OSAL API which are not called on startup.  These are listed in the OSAL API docs and should be copied here.  

### Other methods (catch all)
I don't know if there is anything with a lower priority than above that we actually need to implement, but if there is, it should go here.  
