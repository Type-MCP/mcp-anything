"""Data models for github MCP server."""

from dataclasses import dataclass
from typing import Any


@dataclass
class SecurityAdvisoriesListGlobalAdvisoriesParams:
    """Parameters for security_advisories_list_global_advisories."""
    ghsa_id: str | None = None
    type: str | None = None
    cve_id: str | None = None
    ecosystem: str | None = None
    severity: str | None = None
    cwes: dict | None = None
    is_withdrawn: bool | None = None
    affects: dict | None = None
    published: str | None = None
    updated: str | None = None
    modified: str | None = None
    epss_percentage: str | None = None
    epss_percentile: str | None = None
    before: str | None = None
    after: str | None = None
    direction: str | None = None
    per_page: int | None = None
    sort: str | None = None

@dataclass
class SecurityAdvisoriesGetGlobalAdvisoryParams:
    """Parameters for security_advisories_get_global_advisory."""
    ghsa_id: str

@dataclass
class AppsCreateFromManifestParams:
    """Parameters for apps_create_from_manifest."""
    code: str

@dataclass
class AppsUpdateWebhookConfigForAppParams:
    """Parameters for apps_update_webhook_config_for_app."""
    url: str | None = None
    content_type: str | None = None
    secret: str | None = None
    insecure_ssl: dict | None = None

@dataclass
class AppsListWebhookDeliveriesParams:
    """Parameters for apps_list_webhook_deliveries."""
    per_page: int | None = None
    cursor: str | None = None

@dataclass
class AppsGetWebhookDeliveryParams:
    """Parameters for apps_get_webhook_delivery."""
    delivery_id: int

@dataclass
class AppsRedeliverWebhookDeliveryParams:
    """Parameters for apps_redeliver_webhook_delivery."""
    delivery_id: int

@dataclass
class GetAppInstallationRequestsParams:
    """Parameters for get_app_installation_requests."""
    per_page: int | None = None
    page: int | None = None

@dataclass
class AppsListInstallationsParams:
    """Parameters for apps_list_installations."""
    per_page: int | None = None
    page: int | None = None
    since: str | None = None
    outdated: str | None = None

@dataclass
class AppsDeleteInstallationParams:
    """Parameters for apps_delete_installation."""
    installation_id: int

@dataclass
class AppsGetInstallationParams:
    """Parameters for apps_get_installation."""
    installation_id: int

@dataclass
class AppsCreateInstallationAccessTokenParams:
    """Parameters for apps_create_installation_access_token."""
    installation_id: int
    repositories: list | None = None
    repository_ids: list | None = None
    permissions: dict | None = None

@dataclass
class AppsUnsuspendInstallationParams:
    """Parameters for apps_unsuspend_installation."""
    installation_id: int

@dataclass
class AppsSuspendInstallationParams:
    """Parameters for apps_suspend_installation."""
    installation_id: int

@dataclass
class AppsDeleteAuthorizationParams:
    """Parameters for apps_delete_authorization."""
    client_id: str
    access_token: str

@dataclass
class AppsCheckTokenParams:
    """Parameters for apps_check_token."""
    client_id: str
    access_token: str

@dataclass
class AppsResetTokenParams:
    """Parameters for apps_reset_token."""
    client_id: str
    access_token: str

@dataclass
class AppsDeleteTokenParams:
    """Parameters for apps_delete_token."""
    client_id: str
    access_token: str

@dataclass
class AppsScopeTokenParams:
    """Parameters for apps_scope_token."""
    client_id: str
    access_token: str
    target: str | None = None
    target_id: int | None = None
    repositories: list | None = None
    repository_ids: list | None = None
    permissions: dict | None = None

@dataclass
class AppsGetBySlugParams:
    """Parameters for apps_get_by_slug."""
    app_slug: str

@dataclass
class ClassroomGetAnAssignmentParams:
    """Parameters for classroom_get_an_assignment."""
    assignment_id: int

@dataclass
class GetAssignmentsByAssignmentIdAcceptedAssignmentsParams:
    """Parameters for get_assignments_by_assignment_id_accepted_assignments."""
    assignment_id: int
    page: int | None = None
    per_page: int | None = None

@dataclass
class ClassroomGetAssignmentGradesParams:
    """Parameters for classroom_get_assignment_grades."""
    assignment_id: int

@dataclass
class ClassroomListClassroomsParams:
    """Parameters for classroom_list_classrooms."""
    page: int | None = None
    per_page: int | None = None

@dataclass
class ClassroomGetAClassroomParams:
    """Parameters for classroom_get_a_classroom."""
    classroom_id: int

@dataclass
class ClassroomListAssignmentsForAClassroomParams:
    """Parameters for classroom_list_assignments_for_a_classroom."""
    classroom_id: int
    page: int | None = None
    per_page: int | None = None

@dataclass
class CodesOfConductGetConductCodeParams:
    """Parameters for codes_of_conduct_get_conduct_code."""
    key: str

@dataclass
class CredentialsRevokeParams:
    """Parameters for credentials_revoke."""
    credentials: list

@dataclass
class PutEnterprisesByEnterpriseActionsCacheRetentionLimitParams:
    """Parameters for put_enterprises_by_enterprise_actions_cache_retention_limit."""
    enterprise: str
    max_cache_retention_days: int | None = None

@dataclass
class GetEnterprisesByEnterpriseActionsCacheRetentionLimitParams:
    """Parameters for get_enterprises_by_enterprise_actions_cache_retention_limit."""
    enterprise: str

@dataclass
class PutEnterprisesByEnterpriseActionsCacheStorageLimitParams:
    """Parameters for put_enterprises_by_enterprise_actions_cache_storage_limit."""
    enterprise: str
    max_cache_size_gb: int | None = None

@dataclass
class GetEnterprisesByEnterpriseActionsCacheStorageLimitParams:
    """Parameters for get_enterprises_by_enterprise_actions_cache_storage_limit."""
    enterprise: str

@dataclass
class PostEnterprisesByEnterpriseActionsOidcCustomizationPropertiesRepoParams:
    """Parameters for post_enterprises_by_enterprise_actions_oidc_customization_properties_repo."""
    enterprise: str
    custom_property_name: str

@dataclass
class GetEnterprisesByEnterpriseActionsOidcCustomizationPropertiesRepoParams:
    """Parameters for get_enterprises_by_enterprise_actions_oidc_customization_properties_repo."""
    enterprise: str

@dataclass
class DeleteEnterprisesByEnterpriseActionsOidcCustomizationPropertiesRepoByCustomPropertyNameParams:
    """Parameters for delete_enterprises_by_enterprise_actions_oidc_customization_properties_repo_by_custom_property_name."""
    enterprise: str
    custom_property_name: str

@dataclass
class CodeSecurityCreateConfigurationForEnterpriseParams:
    """Parameters for code_security_create_configuration_for_enterprise."""
    enterprise: str
    name: str
    description: str
    advanced_security: str | None = None
    code_security: str | None = None
    dependency_graph: str | None = None
    dependency_graph_autosubmit_action: str | None = None
    dependency_graph_autosubmit_action_options: dict | None = None
    dependabot_alerts: str | None = None
    dependabot_security_updates: str | None = None
    code_scanning_options: dict | None = None
    code_scanning_default_setup: str | None = None
    code_scanning_default_setup_options: dict | None = None
    code_scanning_delegated_alert_dismissal: str | None = None
    secret_protection: str | None = None
    secret_scanning: str | None = None
    secret_scanning_push_protection: str | None = None
    secret_scanning_validity_checks: str | None = None
    secret_scanning_non_provider_patterns: str | None = None
    secret_scanning_generic_secrets: str | None = None
    secret_scanning_delegated_alert_dismissal: str | None = None
    secret_scanning_extended_metadata: str | None = None
    private_vulnerability_reporting: str | None = None
    enforcement: str | None = None

@dataclass
class CodeSecurityGetConfigurationsForEnterpriseParams:
    """Parameters for code_security_get_configurations_for_enterprise."""
    enterprise: str
    per_page: int | None = None
    before: str | None = None
    after: str | None = None

@dataclass
class GetEnterprisesByEnterpriseCodeSecurityConfigurationsDefaultsParams:
    """Parameters for get_enterprises_by_enterprise_code_security_configurations_defaults."""
    enterprise: str

@dataclass
class CodeSecurityUpdateEnterpriseConfigurationParams:
    """Parameters for code_security_update_enterprise_configuration."""
    enterprise: str
    configuration_id: int
    name: str | None = None
    description: str | None = None
    advanced_security: str | None = None
    code_security: str | None = None
    dependency_graph: str | None = None
    dependency_graph_autosubmit_action: str | None = None
    dependency_graph_autosubmit_action_options: dict | None = None
    dependabot_alerts: str | None = None
    dependabot_security_updates: str | None = None
    code_scanning_default_setup: str | None = None
    code_scanning_default_setup_options: dict | None = None
    code_scanning_options: dict | None = None
    code_scanning_delegated_alert_dismissal: str | None = None
    secret_protection: str | None = None
    secret_scanning: str | None = None
    secret_scanning_push_protection: str | None = None
    secret_scanning_validity_checks: str | None = None
    secret_scanning_non_provider_patterns: str | None = None
    secret_scanning_generic_secrets: str | None = None
    secret_scanning_delegated_alert_dismissal: str | None = None
    secret_scanning_extended_metadata: str | None = None
    private_vulnerability_reporting: str | None = None
    enforcement: str | None = None

@dataclass
class CodeSecurityDeleteConfigurationForEnterpriseParams:
    """Parameters for code_security_delete_configuration_for_enterprise."""
    enterprise: str
    configuration_id: int

@dataclass
class GetEnterprisesByEnterpriseCodeSecurityConfigurationsByConfigurationIdParams:
    """Parameters for get_enterprises_by_enterprise_code_security_configurations_by_configuration_id."""
    enterprise: str
    configuration_id: int

@dataclass
class CodeSecurityAttachEnterpriseConfigurationParams:
    """Parameters for code_security_attach_enterprise_configuration."""
    enterprise: str
    configuration_id: int
    scope: str

@dataclass
class PutEnterprisesByEnterpriseCodeSecurityConfigurationsByConfigurationIdDefaultsParams:
    """Parameters for put_enterprises_by_enterprise_code_security_configurations_by_configuration_id_defaults."""
    enterprise: str
    configuration_id: int
    default_for_new_repos: str | None = None

@dataclass
class GetEnterprisesByEnterpriseCodeSecurityConfigurationsByConfigurationIdRepositoriesParams:
    """Parameters for get_enterprises_by_enterprise_code_security_configurations_by_configuration_id_repositories."""
    enterprise: str
    configuration_id: int
    per_page: int | None = None
    before: str | None = None
    after: str | None = None
    status: str | None = None

@dataclass
class DependabotListAlertsForEnterpriseParams:
    """Parameters for dependabot_list_alerts_for_enterprise."""
    enterprise: str
    state: str | None = None
    severity: str | None = None
    ecosystem: str | None = None
    package: str | None = None
    epss_percentage: str | None = None
    has: dict | None = None
    assignee: str | None = None
    scope: str | None = None
    sort: str | None = None
    direction: str | None = None
    before: str | None = None
    after: str | None = None
    per_page: int | None = None

@dataclass
class EnterpriseTeamsCreateParams:
    """Parameters for enterprise_teams_create."""
    enterprise: str
    name: str
    description: str | None = None
    sync_to_organizations: str | None = None
    organization_selection_type: str | None = None
    group_id: str | None = None

@dataclass
class EnterpriseTeamsListParams:
    """Parameters for enterprise_teams_list."""
    enterprise: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class EnterpriseTeamMembershipsListParams:
    """Parameters for enterprise_team_memberships_list."""
    enterprise: str
    enterprise_team: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class EnterpriseTeamMembershipsBulkAddParams:
    """Parameters for enterprise_team_memberships_bulk_add."""
    enterprise: str
    enterprise_team: str
    usernames: list

@dataclass
class EnterpriseTeamMembershipsBulkRemoveParams:
    """Parameters for enterprise_team_memberships_bulk_remove."""
    enterprise: str
    enterprise_team: str
    usernames: list

@dataclass
class EnterpriseTeamMembershipsRemoveParams:
    """Parameters for enterprise_team_memberships_remove."""
    enterprise: str
    enterprise_team: str
    username: str

@dataclass
class EnterpriseTeamMembershipsAddParams:
    """Parameters for enterprise_team_memberships_add."""
    enterprise: str
    enterprise_team: str
    username: str

@dataclass
class EnterpriseTeamMembershipsGetParams:
    """Parameters for enterprise_team_memberships_get."""
    enterprise: str
    enterprise_team: str
    username: str

@dataclass
class EnterpriseTeamOrganizationsGetAssignmentsParams:
    """Parameters for enterprise_team_organizations_get_assignments."""
    enterprise: str
    enterprise_team: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class EnterpriseTeamOrganizationsBulkAddParams:
    """Parameters for enterprise_team_organizations_bulk_add."""
    enterprise: str
    enterprise_team: str
    organization_slugs: list

@dataclass
class EnterpriseTeamOrganizationsBulkRemoveParams:
    """Parameters for enterprise_team_organizations_bulk_remove."""
    enterprise: str
    enterprise_team: str
    organization_slugs: list

@dataclass
class EnterpriseTeamOrganizationsDeleteParams:
    """Parameters for enterprise_team_organizations_delete."""
    enterprise: str
    enterprise_team: str
    org: str

@dataclass
class EnterpriseTeamOrganizationsAddParams:
    """Parameters for enterprise_team_organizations_add."""
    enterprise: str
    enterprise_team: str
    org: str

@dataclass
class EnterpriseTeamOrganizationsGetAssignmentParams:
    """Parameters for enterprise_team_organizations_get_assignment."""
    enterprise: str
    enterprise_team: str
    org: str

@dataclass
class EnterpriseTeamsUpdateParams:
    """Parameters for enterprise_teams_update."""
    enterprise: str
    team_slug: str
    name: str | None = None
    description: str | None = None
    sync_to_organizations: str | None = None
    organization_selection_type: str | None = None
    group_id: str | None = None

@dataclass
class EnterpriseTeamsDeleteParams:
    """Parameters for enterprise_teams_delete."""
    enterprise: str
    team_slug: str

@dataclass
class EnterpriseTeamsGetParams:
    """Parameters for enterprise_teams_get."""
    enterprise: str
    team_slug: str

@dataclass
class ActivityListPublicEventsParams:
    """Parameters for activity_list_public_events."""
    per_page: int | None = None
    page: int | None = None

@dataclass
class GistsCreateParams:
    """Parameters for gists_create."""
    description: str | None = None
    files: dict
    public: dict | None = None

@dataclass
class GistsListParams:
    """Parameters for gists_list."""
    since: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class GistsListPublicParams:
    """Parameters for gists_list_public."""
    since: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class GistsListStarredParams:
    """Parameters for gists_list_starred."""
    since: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class GistsUpdateParams:
    """Parameters for gists_update."""
    gist_id: str
    description: str | None = None
    files: dict | None = None

@dataclass
class GistsDeleteParams:
    """Parameters for gists_delete."""
    gist_id: str

@dataclass
class GistsGetParams:
    """Parameters for gists_get."""
    gist_id: str

@dataclass
class GistsCreateCommentParams:
    """Parameters for gists_create_comment."""
    gist_id: str
    body: str

@dataclass
class GistsListCommentsParams:
    """Parameters for gists_list_comments."""
    gist_id: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class GistsUpdateCommentParams:
    """Parameters for gists_update_comment."""
    gist_id: str
    comment_id: int
    body: str

@dataclass
class GistsDeleteCommentParams:
    """Parameters for gists_delete_comment."""
    gist_id: str
    comment_id: int

@dataclass
class GistsGetCommentParams:
    """Parameters for gists_get_comment."""
    gist_id: str
    comment_id: int

@dataclass
class GistsListCommitsParams:
    """Parameters for gists_list_commits."""
    gist_id: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class GistsForkParams:
    """Parameters for gists_fork."""
    gist_id: str

@dataclass
class GistsListForksParams:
    """Parameters for gists_list_forks."""
    gist_id: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class GistsUnstarParams:
    """Parameters for gists_unstar."""
    gist_id: str

@dataclass
class GistsStarParams:
    """Parameters for gists_star."""
    gist_id: str

@dataclass
class GistsCheckIsStarredParams:
    """Parameters for gists_check_is_starred."""
    gist_id: str

@dataclass
class GistsGetRevisionParams:
    """Parameters for gists_get_revision."""
    gist_id: str
    sha: str

@dataclass
class GitignoreGetTemplateParams:
    """Parameters for gitignore_get_template."""
    name: str

@dataclass
class AppsListReposAccessibleToInstallationParams:
    """Parameters for apps_list_repos_accessible_to_installation."""
    per_page: int | None = None
    page: int | None = None

@dataclass
class IssuesListParams:
    """Parameters for issues_list."""
    filter: str | None = None
    state: str | None = None
    labels: str | None = None
    sort: str | None = None
    direction: str | None = None
    since: str | None = None
    collab: bool | None = None
    orgs: bool | None = None
    owned: bool | None = None
    pulls: bool | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class LicensesGetAllCommonlyUsedParams:
    """Parameters for licenses_get_all_commonly_used."""
    featured: bool | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class LicensesGetParams:
    """Parameters for licenses_get."""
    license: str

@dataclass
class MarkdownRenderParams:
    """Parameters for markdown_render."""
    text: str
    mode: str | None = None
    context: str | None = None

@dataclass
class AppsGetSubscriptionPlanForAccountParams:
    """Parameters for apps_get_subscription_plan_for_account."""
    account_id: int

@dataclass
class AppsListPlansParams:
    """Parameters for apps_list_plans."""
    per_page: int | None = None
    page: int | None = None

@dataclass
class AppsListAccountsForPlanParams:
    """Parameters for apps_list_accounts_for_plan."""
    plan_id: int
    sort: str | None = None
    direction: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class AppsGetSubscriptionPlanForAccountStubbedParams:
    """Parameters for apps_get_subscription_plan_for_account_stubbed."""
    account_id: int

@dataclass
class AppsListPlansStubbedParams:
    """Parameters for apps_list_plans_stubbed."""
    per_page: int | None = None
    page: int | None = None

@dataclass
class AppsListAccountsForPlanStubbedParams:
    """Parameters for apps_list_accounts_for_plan_stubbed."""
    plan_id: int
    sort: str | None = None
    direction: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActivityListPublicEventsForRepoNetworkParams:
    """Parameters for activity_list_public_events_for_repo_network."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActivityMarkNotificationsAsReadParams:
    """Parameters for activity_mark_notifications_as_read."""
    last_read_at: str | None = None
    read: bool | None = None

@dataclass
class GetNotificationsParams:
    """Parameters for get_notifications."""
    all: bool | None = None
    participating: bool | None = None
    since: str | None = None
    before: str | None = None
    page: int | None = None
    per_page: int | None = None

@dataclass
class ActivityMarkThreadAsReadParams:
    """Parameters for activity_mark_thread_as_read."""
    thread_id: int

@dataclass
class ActivityMarkThreadAsDoneParams:
    """Parameters for activity_mark_thread_as_done."""
    thread_id: int

@dataclass
class ActivityGetThreadParams:
    """Parameters for activity_get_thread."""
    thread_id: int

@dataclass
class ActivityDeleteThreadSubscriptionParams:
    """Parameters for activity_delete_thread_subscription."""
    thread_id: int

@dataclass
class ActivitySetThreadSubscriptionParams:
    """Parameters for activity_set_thread_subscription."""
    thread_id: int
    ignored: bool | None = None

@dataclass
class GetNotificationsThreadsByThreadIdSubscriptionParams:
    """Parameters for get_notifications_threads_by_thread_id_subscription."""
    thread_id: int

@dataclass
class MetaGetOctocatParams:
    """Parameters for meta_get_octocat."""
    s: str | None = None

@dataclass
class OrgsListParams:
    """Parameters for orgs_list."""
    since: int | None = None
    per_page: int | None = None

@dataclass
class PutOrganizationsByOrgActionsCacheRetentionLimitParams:
    """Parameters for put_organizations_by_org_actions_cache_retention_limit."""
    org: str
    max_cache_retention_days: int | None = None

@dataclass
class GetOrganizationsByOrgActionsCacheRetentionLimitParams:
    """Parameters for get_organizations_by_org_actions_cache_retention_limit."""
    org: str

@dataclass
class PutOrganizationsByOrgActionsCacheStorageLimitParams:
    """Parameters for put_organizations_by_org_actions_cache_storage_limit."""
    org: str
    max_cache_size_gb: int | None = None

@dataclass
class GetOrganizationsByOrgActionsCacheStorageLimitParams:
    """Parameters for get_organizations_by_org_actions_cache_storage_limit."""
    org: str

@dataclass
class DependabotUpdateRepositoryAccessForOrgParams:
    """Parameters for dependabot_update_repository_access_for_org."""
    org: str
    repository_ids_to_add: list | None = None
    repository_ids_to_remove: list | None = None

@dataclass
class DependabotRepositoryAccessForOrgParams:
    """Parameters for dependabot_repository_access_for_org."""
    org: str
    page: int | None = None
    per_page: int | None = None

@dataclass
class DependabotSetRepositoryAccessDefaultLevelParams:
    """Parameters for dependabot_set_repository_access_default_level."""
    org: str
    default_level: str

@dataclass
class BillingGetAllBudgetsOrgParams:
    """Parameters for billing_get_all_budgets_org."""
    org: str
    page: int | None = None
    per_page: int | None = None
    scope: str | None = None

@dataclass
class BillingUpdateBudgetOrgParams:
    """Parameters for billing_update_budget_org."""
    org: str
    budget_id: str
    budget_amount: int | None = None
    prevent_further_usage: bool | None = None
    budget_alerting: dict | None = None
    budget_scope: str | None = None
    budget_entity_name: str | None = None
    budget_type: dict | None = None
    budget_product_sku: str | None = None

@dataclass
class BillingDeleteBudgetOrgParams:
    """Parameters for billing_delete_budget_org."""
    org: str
    budget_id: str

@dataclass
class BillingGetBudgetOrgParams:
    """Parameters for billing_get_budget_org."""
    org: str
    budget_id: str

@dataclass
class GetOrganizationsByOrgSettingsBillingPremiumRequestUsageParams:
    """Parameters for get_organizations_by_org_settings_billing_premium_request_usage."""
    org: str
    year: int | None = None
    month: int | None = None
    day: int | None = None
    user: str | None = None
    model: str | None = None
    product: str | None = None

@dataclass
class BillingGetGithubBillingUsageReportOrgParams:
    """Parameters for billing_get_github_billing_usage_report_org."""
    org: str
    year: int | None = None
    month: int | None = None
    day: int | None = None

@dataclass
class GetOrganizationsByOrgSettingsBillingUsageSummaryParams:
    """Parameters for get_organizations_by_org_settings_billing_usage_summary."""
    org: str
    year: int | None = None
    month: int | None = None
    day: int | None = None
    repository: str | None = None
    product: str | None = None
    sku: str | None = None

@dataclass
class OrgsUpdateParams:
    """Parameters for orgs_update."""
    org: str
    billing_email: str | None = None
    company: str | None = None
    email: str | None = None
    twitter_username: str | None = None
    location: str | None = None
    name: str | None = None
    description: str | None = None
    has_organization_projects: bool | None = None
    has_repository_projects: bool | None = None
    default_repository_permission: str | None = None
    members_can_create_repositories: bool | None = None
    members_can_create_internal_repositories: bool | None = None
    members_can_create_private_repositories: bool | None = None
    members_can_create_public_repositories: bool | None = None
    members_allowed_repository_creation_type: str | None = None
    members_can_create_pages: bool | None = None
    members_can_create_public_pages: bool | None = None
    members_can_create_private_pages: bool | None = None
    members_can_fork_private_repositories: bool | None = None
    web_commit_signoff_required: bool | None = None
    blog: str | None = None
    advanced_security_enabled_for_new_repositories: bool | None = None
    dependabot_alerts_enabled_for_new_repositories: bool | None = None
    dependabot_security_updates_enabled_for_new_repositories: bool | None = None
    dependency_graph_enabled_for_new_repositories: bool | None = None
    secret_scanning_enabled_for_new_repositories: bool | None = None
    secret_scanning_push_protection_enabled_for_new_repositories: bool | None = None
    secret_scanning_push_protection_custom_link_enabled: bool | None = None
    secret_scanning_push_protection_custom_link: str | None = None
    deploy_keys_enabled_for_repositories: bool | None = None

@dataclass
class OrgsDeleteParams:
    """Parameters for orgs_delete."""
    org: str

@dataclass
class OrgsGetParams:
    """Parameters for orgs_get."""
    org: str

@dataclass
class ActionsGetActionsCacheUsageForOrgParams:
    """Parameters for actions_get_actions_cache_usage_for_org."""
    org: str

@dataclass
class ActionsGetActionsCacheUsageByRepoForOrgParams:
    """Parameters for actions_get_actions_cache_usage_by_repo_for_org."""
    org: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActionsCreateHostedRunnerForOrgParams:
    """Parameters for actions_create_hosted_runner_for_org."""
    org: str
    name: str
    image: dict
    size: str
    runner_group_id: int
    maximum_runners: int | None = None
    enable_static_ip: bool | None = None
    image_gen: bool | None = None

@dataclass
class ActionsListHostedRunnersForOrgParams:
    """Parameters for actions_list_hosted_runners_for_org."""
    org: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActionsListCustomImagesForOrgParams:
    """Parameters for actions_list_custom_images_for_org."""
    org: str

@dataclass
class ActionsDeleteCustomImageFromOrgParams:
    """Parameters for actions_delete_custom_image_from_org."""
    org: str
    image_definition_id: int

@dataclass
class ActionsGetCustomImageForOrgParams:
    """Parameters for actions_get_custom_image_for_org."""
    org: str
    image_definition_id: int

@dataclass
class ActionsListCustomImageVersionsForOrgParams:
    """Parameters for actions_list_custom_image_versions_for_org."""
    image_definition_id: int
    org: str

@dataclass
class ActionsDeleteCustomImageVersionFromOrgParams:
    """Parameters for actions_delete_custom_image_version_from_org."""
    org: str
    image_definition_id: int
    version: str

@dataclass
class ActionsGetCustomImageVersionForOrgParams:
    """Parameters for actions_get_custom_image_version_for_org."""
    org: str
    image_definition_id: int
    version: str

@dataclass
class GetOrgsByOrgActionsHostedRunnersImagesGithubOwnedParams:
    """Parameters for get_orgs_by_org_actions_hosted_runners_images_github_owned."""
    org: str

@dataclass
class ActionsGetHostedRunnersPartnerImagesForOrgParams:
    """Parameters for actions_get_hosted_runners_partner_images_for_org."""
    org: str

@dataclass
class ActionsGetHostedRunnersLimitsForOrgParams:
    """Parameters for actions_get_hosted_runners_limits_for_org."""
    org: str

@dataclass
class ActionsGetHostedRunnersMachineSpecsForOrgParams:
    """Parameters for actions_get_hosted_runners_machine_specs_for_org."""
    org: str

@dataclass
class ActionsGetHostedRunnersPlatformsForOrgParams:
    """Parameters for actions_get_hosted_runners_platforms_for_org."""
    org: str

@dataclass
class ActionsUpdateHostedRunnerForOrgParams:
    """Parameters for actions_update_hosted_runner_for_org."""
    org: str
    hosted_runner_id: int
    name: str | None = None
    runner_group_id: int | None = None
    maximum_runners: int | None = None
    enable_static_ip: bool | None = None
    size: str | None = None
    image_id: str | None = None
    image_version: str | None = None

@dataclass
class ActionsDeleteHostedRunnerForOrgParams:
    """Parameters for actions_delete_hosted_runner_for_org."""
    org: str
    hosted_runner_id: int

@dataclass
class ActionsGetHostedRunnerForOrgParams:
    """Parameters for actions_get_hosted_runner_for_org."""
    org: str
    hosted_runner_id: int

@dataclass
class PostOrgsByOrgActionsOidcCustomizationPropertiesRepoParams:
    """Parameters for post_orgs_by_org_actions_oidc_customization_properties_repo."""
    org: str
    custom_property_name: str

@dataclass
class OidcListOidcCustomPropertyInclusionsForOrgParams:
    """Parameters for oidc_list_oidc_custom_property_inclusions_for_org."""
    org: str

@dataclass
class DeleteOrgsByOrgActionsOidcCustomizationPropertiesRepoByCustomPropertyNameParams:
    """Parameters for delete_orgs_by_org_actions_oidc_customization_properties_repo_by_custom_property_name."""
    org: str
    custom_property_name: str

@dataclass
class OidcUpdateOidcCustomSubTemplateForOrgParams:
    """Parameters for oidc_update_oidc_custom_sub_template_for_org."""
    org: str
    include_claim_keys: list

@dataclass
class OidcGetOidcCustomSubTemplateForOrgParams:
    """Parameters for oidc_get_oidc_custom_sub_template_for_org."""
    org: str

@dataclass
class PutOrgsByOrgActionsPermissionsParams:
    """Parameters for put_orgs_by_org_actions_permissions."""
    org: str
    enabled_repositories: str
    allowed_actions: str | None = None
    sha_pinning_required: bool | None = None

@dataclass
class GetOrgsByOrgActionsPermissionsParams:
    """Parameters for get_orgs_by_org_actions_permissions."""
    org: str

@dataclass
class PutOrgsByOrgActionsPermissionsArtifactAndLogRetentionParams:
    """Parameters for put_orgs_by_org_actions_permissions_artifact_and_log_retention."""
    org: str
    days: int

@dataclass
class GetOrgsByOrgActionsPermissionsArtifactAndLogRetentionParams:
    """Parameters for get_orgs_by_org_actions_permissions_artifact_and_log_retention."""
    org: str

@dataclass
class PutOrgsByOrgActionsPermissionsForkPrContributorApprovalParams:
    """Parameters for put_orgs_by_org_actions_permissions_fork_pr_contributor_approval."""
    org: str
    approval_policy: str

@dataclass
class GetOrgsByOrgActionsPermissionsForkPrContributorApprovalParams:
    """Parameters for get_orgs_by_org_actions_permissions_fork_pr_contributor_approval."""
    org: str

@dataclass
class PutOrgsByOrgActionsPermissionsForkPrWorkflowsPrivateReposParams:
    """Parameters for put_orgs_by_org_actions_permissions_fork_pr_workflows_private_repos."""
    org: str
    run_workflows_from_fork_pull_requests: bool
    send_write_tokens_to_workflows: bool | None = None
    send_secrets_and_variables: bool | None = None
    require_approval_for_fork_pr_workflows: bool | None = None

@dataclass
class GetOrgsByOrgActionsPermissionsForkPrWorkflowsPrivateReposParams:
    """Parameters for get_orgs_by_org_actions_permissions_fork_pr_workflows_private_repos."""
    org: str

@dataclass
class PutOrgsByOrgActionsPermissionsRepositoriesParams:
    """Parameters for put_orgs_by_org_actions_permissions_repositories."""
    org: str
    selected_repository_ids: list

@dataclass
class GetOrgsByOrgActionsPermissionsRepositoriesParams:
    """Parameters for get_orgs_by_org_actions_permissions_repositories."""
    org: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class DeleteOrgsByOrgActionsPermissionsRepositoriesByRepositoryIdParams:
    """Parameters for delete_orgs_by_org_actions_permissions_repositories_by_repository_id."""
    org: str
    repository_id: int

@dataclass
class PutOrgsByOrgActionsPermissionsRepositoriesByRepositoryIdParams:
    """Parameters for put_orgs_by_org_actions_permissions_repositories_by_repository_id."""
    org: str
    repository_id: int

@dataclass
class ActionsSetAllowedActionsOrganizationParams:
    """Parameters for actions_set_allowed_actions_organization."""
    org: str
    github_owned_allowed: bool | None = None
    verified_allowed: bool | None = None
    patterns_allowed: list | None = None

@dataclass
class ActionsGetAllowedActionsOrganizationParams:
    """Parameters for actions_get_allowed_actions_organization."""
    org: str

@dataclass
class PutOrgsByOrgActionsPermissionsSelfHostedRunnersParams:
    """Parameters for put_orgs_by_org_actions_permissions_self_hosted_runners."""
    org: str
    enabled_repositories: str

@dataclass
class GetOrgsByOrgActionsPermissionsSelfHostedRunnersParams:
    """Parameters for get_orgs_by_org_actions_permissions_self_hosted_runners."""
    org: str

@dataclass
class PutOrgsByOrgActionsPermissionsSelfHostedRunnersRepositoriesParams:
    """Parameters for put_orgs_by_org_actions_permissions_self_hosted_runners_repositories."""
    org: str
    selected_repository_ids: list

@dataclass
class GetOrgsByOrgActionsPermissionsSelfHostedRunnersRepositoriesParams:
    """Parameters for get_orgs_by_org_actions_permissions_self_hosted_runners_repositories."""
    org: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class DeleteOrgsByOrgActionsPermissionsSelfHostedRunnersRepositoriesByRepositoryIdParams:
    """Parameters for delete_orgs_by_org_actions_permissions_self_hosted_runners_repositories_by_repository_id."""
    org: str
    repository_id: int

@dataclass
class PutOrgsByOrgActionsPermissionsSelfHostedRunnersRepositoriesByRepositoryIdParams:
    """Parameters for put_orgs_by_org_actions_permissions_self_hosted_runners_repositories_by_repository_id."""
    org: str
    repository_id: int

@dataclass
class PutOrgsByOrgActionsPermissionsWorkflowParams:
    """Parameters for put_orgs_by_org_actions_permissions_workflow."""
    org: str
    default_workflow_permissions: str | None = None
    can_approve_pull_request_reviews: bool | None = None

@dataclass
class GetOrgsByOrgActionsPermissionsWorkflowParams:
    """Parameters for get_orgs_by_org_actions_permissions_workflow."""
    org: str

@dataclass
class ActionsCreateSelfHostedRunnerGroupForOrgParams:
    """Parameters for actions_create_self_hosted_runner_group_for_org."""
    org: str
    name: str
    visibility: str | None = None
    selected_repository_ids: list | None = None
    runners: list | None = None
    allows_public_repositories: bool | None = None
    restricted_to_workflows: bool | None = None
    selected_workflows: list | None = None
    network_configuration_id: str | None = None

@dataclass
class ActionsListSelfHostedRunnerGroupsForOrgParams:
    """Parameters for actions_list_self_hosted_runner_groups_for_org."""
    org: str
    per_page: int | None = None
    page: int | None = None
    visible_to_repository: str | None = None

@dataclass
class ActionsUpdateSelfHostedRunnerGroupForOrgParams:
    """Parameters for actions_update_self_hosted_runner_group_for_org."""
    org: str
    runner_group_id: int
    name: str
    visibility: str | None = None
    allows_public_repositories: bool | None = None
    restricted_to_workflows: bool | None = None
    selected_workflows: list | None = None
    network_configuration_id: str | None = None

@dataclass
class ActionsDeleteSelfHostedRunnerGroupFromOrgParams:
    """Parameters for actions_delete_self_hosted_runner_group_from_org."""
    org: str
    runner_group_id: int

@dataclass
class ActionsGetSelfHostedRunnerGroupForOrgParams:
    """Parameters for actions_get_self_hosted_runner_group_for_org."""
    org: str
    runner_group_id: int

@dataclass
class GetOrgsByOrgActionsRunnerGroupsByRunnerGroupIdHostedRunnersParams:
    """Parameters for get_orgs_by_org_actions_runner_groups_by_runner_group_id_hosted_runners."""
    org: str
    runner_group_id: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class PutOrgsByOrgActionsRunnerGroupsByRunnerGroupIdRepositoriesParams:
    """Parameters for put_orgs_by_org_actions_runner_groups_by_runner_group_id_repositories."""
    org: str
    runner_group_id: int
    selected_repository_ids: list

@dataclass
class GetOrgsByOrgActionsRunnerGroupsByRunnerGroupIdRepositoriesParams:
    """Parameters for get_orgs_by_org_actions_runner_groups_by_runner_group_id_repositories."""
    org: str
    runner_group_id: int
    page: int | None = None
    per_page: int | None = None

@dataclass
class DeleteOrgsByOrgActionsRunnerGroupsByRunnerGroupIdRepositoriesByRepositoryIdParams:
    """Parameters for delete_orgs_by_org_actions_runner_groups_by_runner_group_id_repositories_by_repository_id."""
    org: str
    runner_group_id: int
    repository_id: int

@dataclass
class PutOrgsByOrgActionsRunnerGroupsByRunnerGroupIdRepositoriesByRepositoryIdParams:
    """Parameters for put_orgs_by_org_actions_runner_groups_by_runner_group_id_repositories_by_repository_id."""
    org: str
    runner_group_id: int
    repository_id: int

@dataclass
class ActionsSetSelfHostedRunnersInGroupForOrgParams:
    """Parameters for actions_set_self_hosted_runners_in_group_for_org."""
    org: str
    runner_group_id: int
    runners: list

@dataclass
class ActionsListSelfHostedRunnersInGroupForOrgParams:
    """Parameters for actions_list_self_hosted_runners_in_group_for_org."""
    org: str
    runner_group_id: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class DeleteOrgsByOrgActionsRunnerGroupsByRunnerGroupIdRunnersByRunnerIdParams:
    """Parameters for delete_orgs_by_org_actions_runner_groups_by_runner_group_id_runners_by_runner_id."""
    org: str
    runner_group_id: int
    runner_id: int

@dataclass
class ActionsAddSelfHostedRunnerToGroupForOrgParams:
    """Parameters for actions_add_self_hosted_runner_to_group_for_org."""
    org: str
    runner_group_id: int
    runner_id: int

@dataclass
class ActionsListSelfHostedRunnersForOrgParams:
    """Parameters for actions_list_self_hosted_runners_for_org."""
    name: str | None = None
    org: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActionsListRunnerApplicationsForOrgParams:
    """Parameters for actions_list_runner_applications_for_org."""
    org: str

@dataclass
class ActionsGenerateRunnerJitconfigForOrgParams:
    """Parameters for actions_generate_runner_jitconfig_for_org."""
    org: str
    name: str
    runner_group_id: int
    labels: list
    work_folder: str | None = None

@dataclass
class ActionsCreateRegistrationTokenForOrgParams:
    """Parameters for actions_create_registration_token_for_org."""
    org: str

@dataclass
class ActionsCreateRemoveTokenForOrgParams:
    """Parameters for actions_create_remove_token_for_org."""
    org: str

@dataclass
class ActionsDeleteSelfHostedRunnerFromOrgParams:
    """Parameters for actions_delete_self_hosted_runner_from_org."""
    org: str
    runner_id: int

@dataclass
class ActionsGetSelfHostedRunnerForOrgParams:
    """Parameters for actions_get_self_hosted_runner_for_org."""
    org: str
    runner_id: int

@dataclass
class PostOrgsByOrgActionsRunnersByRunnerIdLabelsParams:
    """Parameters for post_orgs_by_org_actions_runners_by_runner_id_labels."""
    org: str
    runner_id: int
    labels: list

@dataclass
class DeleteOrgsByOrgActionsRunnersByRunnerIdLabelsParams:
    """Parameters for delete_orgs_by_org_actions_runners_by_runner_id_labels."""
    org: str
    runner_id: int

@dataclass
class PutOrgsByOrgActionsRunnersByRunnerIdLabelsParams:
    """Parameters for put_orgs_by_org_actions_runners_by_runner_id_labels."""
    org: str
    runner_id: int
    labels: list

@dataclass
class GetOrgsByOrgActionsRunnersByRunnerIdLabelsParams:
    """Parameters for get_orgs_by_org_actions_runners_by_runner_id_labels."""
    org: str
    runner_id: int

@dataclass
class DeleteOrgsByOrgActionsRunnersByRunnerIdLabelsByNameParams:
    """Parameters for delete_orgs_by_org_actions_runners_by_runner_id_labels_by_name."""
    org: str
    runner_id: int
    name: str

@dataclass
class ActionsListOrgSecretsParams:
    """Parameters for actions_list_org_secrets."""
    org: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActionsGetOrgPublicKeyParams:
    """Parameters for actions_get_org_public_key."""
    org: str

@dataclass
class ActionsDeleteOrgSecretParams:
    """Parameters for actions_delete_org_secret."""
    org: str
    secret_name: str

@dataclass
class ActionsCreateOrUpdateOrgSecretParams:
    """Parameters for actions_create_or_update_org_secret."""
    org: str
    secret_name: str
    encrypted_value: str
    key_id: str
    visibility: str
    selected_repository_ids: list | None = None

@dataclass
class ActionsGetOrgSecretParams:
    """Parameters for actions_get_org_secret."""
    org: str
    secret_name: str

@dataclass
class ActionsSetSelectedReposForOrgSecretParams:
    """Parameters for actions_set_selected_repos_for_org_secret."""
    org: str
    secret_name: str
    selected_repository_ids: list

@dataclass
class ActionsListSelectedReposForOrgSecretParams:
    """Parameters for actions_list_selected_repos_for_org_secret."""
    org: str
    secret_name: str
    page: int | None = None
    per_page: int | None = None

@dataclass
class ActionsRemoveSelectedRepoFromOrgSecretParams:
    """Parameters for actions_remove_selected_repo_from_org_secret."""
    org: str
    secret_name: str
    repository_id: int

@dataclass
class ActionsAddSelectedRepoToOrgSecretParams:
    """Parameters for actions_add_selected_repo_to_org_secret."""
    org: str
    secret_name: str
    repository_id: int

@dataclass
class ActionsCreateOrgVariableParams:
    """Parameters for actions_create_org_variable."""
    org: str
    name: str
    value: str
    visibility: str
    selected_repository_ids: list | None = None

@dataclass
class ActionsListOrgVariablesParams:
    """Parameters for actions_list_org_variables."""
    org: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActionsUpdateOrgVariableParams:
    """Parameters for actions_update_org_variable."""
    org: str
    name: str
    value: str | None = None
    visibility: str | None = None
    selected_repository_ids: list | None = None

@dataclass
class ActionsDeleteOrgVariableParams:
    """Parameters for actions_delete_org_variable."""
    org: str
    name: str

@dataclass
class ActionsGetOrgVariableParams:
    """Parameters for actions_get_org_variable."""
    org: str
    name: str

@dataclass
class ActionsSetSelectedReposForOrgVariableParams:
    """Parameters for actions_set_selected_repos_for_org_variable."""
    org: str
    name: str
    selected_repository_ids: list

@dataclass
class ActionsListSelectedReposForOrgVariableParams:
    """Parameters for actions_list_selected_repos_for_org_variable."""
    org: str
    name: str
    page: int | None = None
    per_page: int | None = None

@dataclass
class ActionsRemoveSelectedRepoFromOrgVariableParams:
    """Parameters for actions_remove_selected_repo_from_org_variable."""
    org: str
    name: str
    repository_id: int

@dataclass
class ActionsAddSelectedRepoToOrgVariableParams:
    """Parameters for actions_add_selected_repo_to_org_variable."""
    org: str
    name: str
    repository_id: int

@dataclass
class OrgsCreateArtifactDeploymentRecordParams:
    """Parameters for orgs_create_artifact_deployment_record."""
    org: str
    name: str
    digest: str
    version: str | None = None
    status: str
    logical_environment: str
    physical_environment: str | None = None
    cluster: str | None = None
    deployment_name: str
    tags: dict | None = None
    runtime_risks: list | None = None
    github_repository: str | None = None

@dataclass
class OrgsSetClusterDeploymentRecordsParams:
    """Parameters for orgs_set_cluster_deployment_records."""
    org: str
    cluster: str
    logical_environment: str
    physical_environment: str | None = None
    deployments: list

@dataclass
class OrgsCreateArtifactStorageRecordParams:
    """Parameters for orgs_create_artifact_storage_record."""
    org: str
    name: str
    digest: str
    version: str | None = None
    artifact_url: str | None = None
    path: str | None = None
    registry_url: str
    repository: str | None = None
    status: str | None = None
    github_repository: str | None = None

@dataclass
class OrgsListArtifactDeploymentRecordsParams:
    """Parameters for orgs_list_artifact_deployment_records."""
    org: str
    subject_digest: str

@dataclass
class OrgsListArtifactStorageRecordsParams:
    """Parameters for orgs_list_artifact_storage_records."""
    org: str
    subject_digest: str

@dataclass
class OrgsListAttestationsBulkParams:
    """Parameters for orgs_list_attestations_bulk."""
    per_page: int | None = None
    before: str | None = None
    after: str | None = None
    org: str
    subject_digests: list
    predicate_type: str | None = None

@dataclass
class OrgsDeleteAttestationsBulkParams:
    """Parameters for orgs_delete_attestations_bulk."""
    org: str
    body: dict

@dataclass
class OrgsDeleteAttestationsBySubjectDigestParams:
    """Parameters for orgs_delete_attestations_by_subject_digest."""
    org: str
    subject_digest: str

@dataclass
class OrgsListAttestationRepositoriesParams:
    """Parameters for orgs_list_attestation_repositories."""
    per_page: int | None = None
    before: str | None = None
    after: str | None = None
    org: str
    predicate_type: str | None = None

@dataclass
class OrgsDeleteAttestationsByIdParams:
    """Parameters for orgs_delete_attestations_by_id."""
    org: str
    attestation_id: int

@dataclass
class OrgsListAttestationsParams:
    """Parameters for orgs_list_attestations."""
    per_page: int | None = None
    before: str | None = None
    after: str | None = None
    org: str
    subject_digest: str
    predicate_type: str | None = None

@dataclass
class OrgsListBlockedUsersParams:
    """Parameters for orgs_list_blocked_users."""
    org: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class OrgsUnblockUserParams:
    """Parameters for orgs_unblock_user."""
    org: str
    username: str

@dataclass
class OrgsBlockUserParams:
    """Parameters for orgs_block_user."""
    org: str
    username: str

@dataclass
class OrgsCheckBlockedUserParams:
    """Parameters for orgs_check_blocked_user."""
    org: str
    username: str

@dataclass
class CampaignsCreateCampaignParams:
    """Parameters for campaigns_create_campaign."""
    org: str
    name: str
    description: str
    managers: list | None = None
    team_managers: list | None = None
    ends_at: str
    contact_link: str | None = None
    code_scanning_alerts: list | None = None
    generate_issues: bool | None = None

@dataclass
class CampaignsListOrgCampaignsParams:
    """Parameters for campaigns_list_org_campaigns."""
    org: str
    page: int | None = None
    per_page: int | None = None
    direction: str | None = None
    state: str | None = None
    sort: str | None = None

@dataclass
class CampaignsUpdateCampaignParams:
    """Parameters for campaigns_update_campaign."""
    org: str
    campaign_number: int
    name: str | None = None
    description: str | None = None
    managers: list | None = None
    team_managers: list | None = None
    ends_at: str | None = None
    contact_link: str | None = None
    state: str | None = None

@dataclass
class CampaignsDeleteCampaignParams:
    """Parameters for campaigns_delete_campaign."""
    org: str
    campaign_number: int

@dataclass
class CampaignsGetCampaignSummaryParams:
    """Parameters for campaigns_get_campaign_summary."""
    org: str
    campaign_number: int

@dataclass
class CodeScanningListAlertsForOrgParams:
    """Parameters for code_scanning_list_alerts_for_org."""
    org: str
    tool_name: str | None = None
    tool_guid: str | None = None
    before: str | None = None
    after: str | None = None
    page: int | None = None
    per_page: int | None = None
    direction: str | None = None
    state: str | None = None
    sort: str | None = None
    severity: str | None = None
    assignees: str | None = None

@dataclass
class CodeSecurityCreateConfigurationParams:
    """Parameters for code_security_create_configuration."""
    org: str
    name: str
    description: str
    advanced_security: str | None = None
    code_security: str | None = None
    dependency_graph: str | None = None
    dependency_graph_autosubmit_action: str | None = None
    dependency_graph_autosubmit_action_options: dict | None = None
    dependabot_alerts: str | None = None
    dependabot_security_updates: str | None = None
    dependabot_delegated_alert_dismissal: str | None = None
    code_scanning_options: dict | None = None
    code_scanning_default_setup: str | None = None
    code_scanning_default_setup_options: dict | None = None
    code_scanning_delegated_alert_dismissal: str | None = None
    secret_protection: str | None = None
    secret_scanning: str | None = None
    secret_scanning_push_protection: str | None = None
    secret_scanning_delegated_bypass: str | None = None
    secret_scanning_delegated_bypass_options: dict | None = None
    secret_scanning_validity_checks: str | None = None
    secret_scanning_non_provider_patterns: str | None = None
    secret_scanning_generic_secrets: str | None = None
    secret_scanning_delegated_alert_dismissal: str | None = None
    secret_scanning_extended_metadata: str | None = None
    private_vulnerability_reporting: str | None = None
    enforcement: str | None = None

@dataclass
class CodeSecurityGetConfigurationsForOrgParams:
    """Parameters for code_security_get_configurations_for_org."""
    org: str
    target_type: str | None = None
    per_page: int | None = None
    before: str | None = None
    after: str | None = None

@dataclass
class CodeSecurityGetDefaultConfigurationsParams:
    """Parameters for code_security_get_default_configurations."""
    org: str

@dataclass
class CodeSecurityDetachConfigurationParams:
    """Parameters for code_security_detach_configuration."""
    org: str
    selected_repository_ids: list | None = None

@dataclass
class CodeSecurityUpdateConfigurationParams:
    """Parameters for code_security_update_configuration."""
    org: str
    configuration_id: int
    name: str | None = None
    description: str | None = None
    advanced_security: str | None = None
    code_security: str | None = None
    dependency_graph: str | None = None
    dependency_graph_autosubmit_action: str | None = None
    dependency_graph_autosubmit_action_options: dict | None = None
    dependabot_alerts: str | None = None
    dependabot_security_updates: str | None = None
    dependabot_delegated_alert_dismissal: str | None = None
    code_scanning_default_setup: str | None = None
    code_scanning_default_setup_options: dict | None = None
    code_scanning_options: dict | None = None
    code_scanning_delegated_alert_dismissal: str | None = None
    secret_protection: str | None = None
    secret_scanning: str | None = None
    secret_scanning_push_protection: str | None = None
    secret_scanning_delegated_bypass: str | None = None
    secret_scanning_delegated_bypass_options: dict | None = None
    secret_scanning_validity_checks: str | None = None
    secret_scanning_non_provider_patterns: str | None = None
    secret_scanning_generic_secrets: str | None = None
    secret_scanning_delegated_alert_dismissal: str | None = None
    secret_scanning_extended_metadata: str | None = None
    private_vulnerability_reporting: str | None = None
    enforcement: str | None = None

@dataclass
class CodeSecurityDeleteConfigurationParams:
    """Parameters for code_security_delete_configuration."""
    org: str
    configuration_id: int

@dataclass
class CodeSecurityGetConfigurationParams:
    """Parameters for code_security_get_configuration."""
    org: str
    configuration_id: int

@dataclass
class CodeSecurityAttachConfigurationParams:
    """Parameters for code_security_attach_configuration."""
    org: str
    configuration_id: int
    scope: str
    selected_repository_ids: list | None = None

@dataclass
class CodeSecuritySetConfigurationAsDefaultParams:
    """Parameters for code_security_set_configuration_as_default."""
    org: str
    configuration_id: int
    default_for_new_repos: str | None = None

@dataclass
class CodeSecurityGetRepositoriesForConfigurationParams:
    """Parameters for code_security_get_repositories_for_configuration."""
    org: str
    configuration_id: int
    per_page: int | None = None
    before: str | None = None
    after: str | None = None
    status: str | None = None

@dataclass
class CodespacesListInOrganizationParams:
    """Parameters for codespaces_list_in_organization."""
    per_page: int | None = None
    page: int | None = None
    org: str

@dataclass
class CodespacesSetCodespacesAccessParams:
    """Parameters for codespaces_set_codespaces_access."""
    org: str
    visibility: str
    selected_usernames: list | None = None

@dataclass
class CodespacesSetCodespacesAccessUsersParams:
    """Parameters for codespaces_set_codespaces_access_users."""
    org: str
    selected_usernames: list

@dataclass
class CodespacesDeleteCodespacesAccessUsersParams:
    """Parameters for codespaces_delete_codespaces_access_users."""
    org: str
    selected_usernames: list

@dataclass
class CodespacesListOrgSecretsParams:
    """Parameters for codespaces_list_org_secrets."""
    org: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class CodespacesGetOrgPublicKeyParams:
    """Parameters for codespaces_get_org_public_key."""
    org: str

@dataclass
class CodespacesDeleteOrgSecretParams:
    """Parameters for codespaces_delete_org_secret."""
    org: str
    secret_name: str

@dataclass
class CodespacesCreateOrUpdateOrgSecretParams:
    """Parameters for codespaces_create_or_update_org_secret."""
    org: str
    secret_name: str
    encrypted_value: str | None = None
    key_id: str | None = None
    visibility: str
    selected_repository_ids: list | None = None

@dataclass
class CodespacesGetOrgSecretParams:
    """Parameters for codespaces_get_org_secret."""
    org: str
    secret_name: str

@dataclass
class CodespacesSetSelectedReposForOrgSecretParams:
    """Parameters for codespaces_set_selected_repos_for_org_secret."""
    org: str
    secret_name: str
    selected_repository_ids: list

@dataclass
class CodespacesListSelectedReposForOrgSecretParams:
    """Parameters for codespaces_list_selected_repos_for_org_secret."""
    org: str
    secret_name: str
    page: int | None = None
    per_page: int | None = None

@dataclass
class CodespacesRemoveSelectedRepoFromOrgSecretParams:
    """Parameters for codespaces_remove_selected_repo_from_org_secret."""
    org: str
    secret_name: str
    repository_id: int

@dataclass
class CodespacesAddSelectedRepoToOrgSecretParams:
    """Parameters for codespaces_add_selected_repo_to_org_secret."""
    org: str
    secret_name: str
    repository_id: int

@dataclass
class CopilotGetCopilotOrganizationDetailsParams:
    """Parameters for copilot_get_copilot_organization_details."""
    org: str

@dataclass
class CopilotListCopilotSeatsParams:
    """Parameters for copilot_list_copilot_seats."""
    org: str
    page: int | None = None
    per_page: int | None = None

@dataclass
class CopilotAddCopilotSeatsForTeamsParams:
    """Parameters for copilot_add_copilot_seats_for_teams."""
    org: str
    selected_teams: list

@dataclass
class CopilotCancelCopilotSeatAssignmentForTeamsParams:
    """Parameters for copilot_cancel_copilot_seat_assignment_for_teams."""
    org: str
    selected_teams: list

@dataclass
class CopilotAddCopilotSeatsForUsersParams:
    """Parameters for copilot_add_copilot_seats_for_users."""
    org: str
    selected_usernames: list

@dataclass
class CopilotCancelCopilotSeatAssignmentForUsersParams:
    """Parameters for copilot_cancel_copilot_seat_assignment_for_users."""
    org: str
    selected_usernames: list

@dataclass
class PutOrgsByOrgCopilotContentExclusionParams:
    """Parameters for put_orgs_by_org_copilot_content_exclusion."""
    org: str
    body: dict

@dataclass
class GetOrgsByOrgCopilotContentExclusionParams:
    """Parameters for get_orgs_by_org_copilot_content_exclusion."""
    org: str

@dataclass
class CopilotCopilotMetricsForOrganizationParams:
    """Parameters for copilot_copilot_metrics_for_organization."""
    org: str
    since: str | None = None
    until: str | None = None
    page: int | None = None
    per_page: int | None = None

@dataclass
class DependabotListAlertsForOrgParams:
    """Parameters for dependabot_list_alerts_for_org."""
    org: str
    state: str | None = None
    severity: str | None = None
    ecosystem: str | None = None
    package: str | None = None
    epss_percentage: str | None = None
    artifact_registry_url: str | None = None
    artifact_registry: str | None = None
    has: dict | None = None
    assignee: str | None = None
    runtime_risk: str | None = None
    scope: str | None = None
    sort: str | None = None
    direction: str | None = None
    before: str | None = None
    after: str | None = None
    per_page: int | None = None

@dataclass
class DependabotListOrgSecretsParams:
    """Parameters for dependabot_list_org_secrets."""
    org: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class DependabotGetOrgPublicKeyParams:
    """Parameters for dependabot_get_org_public_key."""
    org: str

@dataclass
class DependabotDeleteOrgSecretParams:
    """Parameters for dependabot_delete_org_secret."""
    org: str
    secret_name: str

@dataclass
class DependabotCreateOrUpdateOrgSecretParams:
    """Parameters for dependabot_create_or_update_org_secret."""
    org: str
    secret_name: str
    encrypted_value: str | None = None
    key_id: str | None = None
    visibility: str
    selected_repository_ids: list | None = None

@dataclass
class DependabotGetOrgSecretParams:
    """Parameters for dependabot_get_org_secret."""
    org: str
    secret_name: str

@dataclass
class DependabotSetSelectedReposForOrgSecretParams:
    """Parameters for dependabot_set_selected_repos_for_org_secret."""
    org: str
    secret_name: str
    selected_repository_ids: list

@dataclass
class DependabotListSelectedReposForOrgSecretParams:
    """Parameters for dependabot_list_selected_repos_for_org_secret."""
    org: str
    secret_name: str
    page: int | None = None
    per_page: int | None = None

@dataclass
class DependabotRemoveSelectedRepoFromOrgSecretParams:
    """Parameters for dependabot_remove_selected_repo_from_org_secret."""
    org: str
    secret_name: str
    repository_id: int

@dataclass
class DependabotAddSelectedRepoToOrgSecretParams:
    """Parameters for dependabot_add_selected_repo_to_org_secret."""
    org: str
    secret_name: str
    repository_id: int

@dataclass
class GetOrgsByOrgDockerConflictsParams:
    """Parameters for get_orgs_by_org_docker_conflicts."""
    org: str

@dataclass
class ActivityListPublicOrgEventsParams:
    """Parameters for activity_list_public_org_events."""
    org: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class OrgsListFailedInvitationsParams:
    """Parameters for orgs_list_failed_invitations."""
    org: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class OrgsCreateWebhookParams:
    """Parameters for orgs_create_webhook."""
    org: str
    name: str
    config: dict
    events: list | None = None
    active: bool | None = None

@dataclass
class OrgsListWebhooksParams:
    """Parameters for orgs_list_webhooks."""
    org: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class OrgsUpdateWebhookParams:
    """Parameters for orgs_update_webhook."""
    org: str
    hook_id: int
    config: dict | None = None
    events: list | None = None
    active: bool | None = None
    name: str | None = None

@dataclass
class OrgsDeleteWebhookParams:
    """Parameters for orgs_delete_webhook."""
    org: str
    hook_id: int

@dataclass
class OrgsGetWebhookParams:
    """Parameters for orgs_get_webhook."""
    org: str
    hook_id: int

@dataclass
class OrgsUpdateWebhookConfigForOrgParams:
    """Parameters for orgs_update_webhook_config_for_org."""
    org: str
    hook_id: int
    url: str | None = None
    content_type: str | None = None
    secret: str | None = None
    insecure_ssl: dict | None = None

@dataclass
class OrgsGetWebhookConfigForOrgParams:
    """Parameters for orgs_get_webhook_config_for_org."""
    org: str
    hook_id: int

@dataclass
class OrgsListWebhookDeliveriesParams:
    """Parameters for orgs_list_webhook_deliveries."""
    org: str
    hook_id: int
    per_page: int | None = None
    cursor: str | None = None

@dataclass
class OrgsGetWebhookDeliveryParams:
    """Parameters for orgs_get_webhook_delivery."""
    org: str
    hook_id: int
    delivery_id: int

@dataclass
class OrgsRedeliverWebhookDeliveryParams:
    """Parameters for orgs_redeliver_webhook_delivery."""
    org: str
    hook_id: int
    delivery_id: int

@dataclass
class OrgsPingWebhookParams:
    """Parameters for orgs_ping_webhook."""
    org: str
    hook_id: int

@dataclass
class ApiInsightsGetRouteStatsByActorParams:
    """Parameters for api_insights_get_route_stats_by_actor."""
    org: str
    actor_type: str
    actor_id: int
    min_timestamp: str
    max_timestamp: str | None = None
    page: int | None = None
    per_page: int | None = None
    direction: str | None = None
    sort: list | None = None
    api_route_substring: str | None = None

@dataclass
class ApiInsightsGetSubjectStatsParams:
    """Parameters for api_insights_get_subject_stats."""
    org: str
    min_timestamp: str
    max_timestamp: str | None = None
    page: int | None = None
    per_page: int | None = None
    direction: str | None = None
    sort: list | None = None
    subject_name_substring: str | None = None

@dataclass
class ApiInsightsGetSummaryStatsParams:
    """Parameters for api_insights_get_summary_stats."""
    org: str
    min_timestamp: str
    max_timestamp: str | None = None

@dataclass
class ApiInsightsGetSummaryStatsByUserParams:
    """Parameters for api_insights_get_summary_stats_by_user."""
    org: str
    user_id: str
    min_timestamp: str
    max_timestamp: str | None = None

@dataclass
class ApiInsightsGetSummaryStatsByActorParams:
    """Parameters for api_insights_get_summary_stats_by_actor."""
    org: str
    min_timestamp: str
    max_timestamp: str | None = None
    actor_type: str
    actor_id: int

@dataclass
class ApiInsightsGetTimeStatsParams:
    """Parameters for api_insights_get_time_stats."""
    org: str
    min_timestamp: str
    max_timestamp: str | None = None
    timestamp_increment: str

@dataclass
class ApiInsightsGetTimeStatsByUserParams:
    """Parameters for api_insights_get_time_stats_by_user."""
    org: str
    user_id: str
    min_timestamp: str
    max_timestamp: str | None = None
    timestamp_increment: str

@dataclass
class ApiInsightsGetTimeStatsByActorParams:
    """Parameters for api_insights_get_time_stats_by_actor."""
    org: str
    actor_type: str
    actor_id: int
    min_timestamp: str
    max_timestamp: str | None = None
    timestamp_increment: str

@dataclass
class ApiInsightsGetUserStatsParams:
    """Parameters for api_insights_get_user_stats."""
    org: str
    user_id: str
    min_timestamp: str
    max_timestamp: str | None = None
    page: int | None = None
    per_page: int | None = None
    direction: str | None = None
    sort: list | None = None
    actor_name_substring: str | None = None

@dataclass
class AppsGetOrgInstallationParams:
    """Parameters for apps_get_org_installation."""
    org: str

@dataclass
class OrgsListAppInstallationsParams:
    """Parameters for orgs_list_app_installations."""
    org: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class InteractionsRemoveRestrictionsForOrgParams:
    """Parameters for interactions_remove_restrictions_for_org."""
    org: str

@dataclass
class InteractionsSetRestrictionsForOrgParams:
    """Parameters for interactions_set_restrictions_for_org."""
    org: str
    limit: str
    expiry: str | None = None

@dataclass
class InteractionsGetRestrictionsForOrgParams:
    """Parameters for interactions_get_restrictions_for_org."""
    org: str

@dataclass
class OrgsCreateInvitationParams:
    """Parameters for orgs_create_invitation."""
    org: str
    invitee_id: int | None = None
    email: str | None = None
    role: str | None = None
    team_ids: list | None = None

@dataclass
class OrgsListPendingInvitationsParams:
    """Parameters for orgs_list_pending_invitations."""
    org: str
    per_page: int | None = None
    page: int | None = None
    role: str | None = None
    invitation_source: str | None = None

@dataclass
class OrgsCancelInvitationParams:
    """Parameters for orgs_cancel_invitation."""
    org: str
    invitation_id: int

@dataclass
class OrgsListInvitationTeamsParams:
    """Parameters for orgs_list_invitation_teams."""
    org: str
    invitation_id: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class OrgsCreateIssueFieldParams:
    """Parameters for orgs_create_issue_field."""
    org: str
    name: str
    description: str | None = None
    data_type: str
    visibility: str | None = None
    options: list | None = None

@dataclass
class OrgsListIssueFieldsParams:
    """Parameters for orgs_list_issue_fields."""
    org: str

@dataclass
class OrgsUpdateIssueFieldParams:
    """Parameters for orgs_update_issue_field."""
    org: str
    issue_field_id: int
    name: str | None = None
    description: str | None = None
    visibility: str | None = None
    options: list | None = None

@dataclass
class OrgsDeleteIssueFieldParams:
    """Parameters for orgs_delete_issue_field."""
    org: str
    issue_field_id: int

@dataclass
class OrgsCreateIssueTypeParams:
    """Parameters for orgs_create_issue_type."""
    org: str
    name: str
    is_enabled: bool
    description: str | None = None
    color: str | None = None

@dataclass
class OrgsListIssueTypesParams:
    """Parameters for orgs_list_issue_types."""
    org: str

@dataclass
class OrgsDeleteIssueTypeParams:
    """Parameters for orgs_delete_issue_type."""
    org: str
    issue_type_id: int

@dataclass
class OrgsUpdateIssueTypeParams:
    """Parameters for orgs_update_issue_type."""
    org: str
    issue_type_id: int
    name: str
    is_enabled: bool
    description: str | None = None
    color: str | None = None

@dataclass
class IssuesListForOrgParams:
    """Parameters for issues_list_for_org."""
    org: str
    filter: str | None = None
    state: str | None = None
    labels: str | None = None
    type: str | None = None
    sort: str | None = None
    direction: str | None = None
    since: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class OrgsListMembersParams:
    """Parameters for orgs_list_members."""
    org: str
    filter: str | None = None
    role: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class OrgsRemoveMemberParams:
    """Parameters for orgs_remove_member."""
    org: str
    username: str

@dataclass
class OrgsCheckMembershipForUserParams:
    """Parameters for orgs_check_membership_for_user."""
    org: str
    username: str

@dataclass
class CodespacesGetCodespacesForUserInOrgParams:
    """Parameters for codespaces_get_codespaces_for_user_in_org."""
    per_page: int | None = None
    page: int | None = None
    org: str
    username: str

@dataclass
class CodespacesDeleteFromOrganizationParams:
    """Parameters for codespaces_delete_from_organization."""
    org: str
    username: str
    codespace_name: str

@dataclass
class CodespacesStopInOrganizationParams:
    """Parameters for codespaces_stop_in_organization."""
    org: str
    username: str
    codespace_name: str

@dataclass
class CopilotGetCopilotSeatDetailsForUserParams:
    """Parameters for copilot_get_copilot_seat_details_for_user."""
    org: str
    username: str

@dataclass
class OrgsRemoveMembershipForUserParams:
    """Parameters for orgs_remove_membership_for_user."""
    org: str
    username: str

@dataclass
class OrgsSetMembershipForUserParams:
    """Parameters for orgs_set_membership_for_user."""
    org: str
    username: str
    role: str | None = None

@dataclass
class OrgsGetMembershipForUserParams:
    """Parameters for orgs_get_membership_for_user."""
    org: str
    username: str

@dataclass
class MigrationsStartForOrgParams:
    """Parameters for migrations_start_for_org."""
    org: str
    repositories: list
    lock_repositories: bool | None = None
    exclude_metadata: bool | None = None
    exclude_git_data: bool | None = None
    exclude_attachments: bool | None = None
    exclude_releases: bool | None = None
    exclude_owner_projects: bool | None = None
    org_metadata_only: bool | None = None
    exclude: list | None = None

@dataclass
class MigrationsListForOrgParams:
    """Parameters for migrations_list_for_org."""
    org: str
    per_page: int | None = None
    page: int | None = None
    exclude: list | None = None

@dataclass
class MigrationsGetStatusForOrgParams:
    """Parameters for migrations_get_status_for_org."""
    org: str
    migration_id: int
    exclude: list | None = None

@dataclass
class MigrationsDeleteArchiveForOrgParams:
    """Parameters for migrations_delete_archive_for_org."""
    org: str
    migration_id: int

@dataclass
class MigrationsDownloadArchiveForOrgParams:
    """Parameters for migrations_download_archive_for_org."""
    org: str
    migration_id: int

@dataclass
class MigrationsUnlockRepoForOrgParams:
    """Parameters for migrations_unlock_repo_for_org."""
    org: str
    migration_id: int
    repo_name: str

@dataclass
class MigrationsListReposForOrgParams:
    """Parameters for migrations_list_repos_for_org."""
    org: str
    migration_id: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class OrgsListOrgRolesParams:
    """Parameters for orgs_list_org_roles."""
    org: str

@dataclass
class OrgsRevokeAllOrgRolesTeamParams:
    """Parameters for orgs_revoke_all_org_roles_team."""
    org: str
    team_slug: str

@dataclass
class OrgsRevokeOrgRoleTeamParams:
    """Parameters for orgs_revoke_org_role_team."""
    org: str
    team_slug: str
    role_id: int

@dataclass
class OrgsAssignTeamToOrgRoleParams:
    """Parameters for orgs_assign_team_to_org_role."""
    org: str
    team_slug: str
    role_id: int

@dataclass
class OrgsRevokeAllOrgRolesUserParams:
    """Parameters for orgs_revoke_all_org_roles_user."""
    org: str
    username: str

@dataclass
class OrgsRevokeOrgRoleUserParams:
    """Parameters for orgs_revoke_org_role_user."""
    org: str
    username: str
    role_id: int

@dataclass
class OrgsAssignUserToOrgRoleParams:
    """Parameters for orgs_assign_user_to_org_role."""
    org: str
    username: str
    role_id: int

@dataclass
class OrgsGetOrgRoleParams:
    """Parameters for orgs_get_org_role."""
    org: str
    role_id: int

@dataclass
class OrgsListOrgRoleTeamsParams:
    """Parameters for orgs_list_org_role_teams."""
    org: str
    role_id: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class OrgsListOrgRoleUsersParams:
    """Parameters for orgs_list_org_role_users."""
    org: str
    role_id: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class OrgsListOutsideCollaboratorsParams:
    """Parameters for orgs_list_outside_collaborators."""
    org: str
    filter: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class OrgsRemoveOutsideCollaboratorParams:
    """Parameters for orgs_remove_outside_collaborator."""
    org: str
    username: str

@dataclass
class OrgsConvertMemberToOutsideCollaboratorParams:
    """Parameters for orgs_convert_member_to_outside_collaborator."""
    org: str
    username: str
    async_: bool | None = None

@dataclass
class PackagesListPackagesForOrganizationParams:
    """Parameters for packages_list_packages_for_organization."""
    package_type: str
    org: str
    visibility: str | None = None
    page: int | None = None
    per_page: int | None = None

@dataclass
class PackagesDeletePackageForOrgParams:
    """Parameters for packages_delete_package_for_org."""
    package_type: str
    package_name: str
    org: str

@dataclass
class PackagesGetPackageForOrganizationParams:
    """Parameters for packages_get_package_for_organization."""
    package_type: str
    package_name: str
    org: str

@dataclass
class PackagesRestorePackageForOrgParams:
    """Parameters for packages_restore_package_for_org."""
    package_type: str
    package_name: str
    org: str
    token: str | None = None

@dataclass
class GetOrgsByOrgPackagesByPackageTypeByPackageNameVersionsParams:
    """Parameters for get_orgs_by_org_packages_by_package_type_by_package_name_versions."""
    package_type: str
    package_name: str
    org: str
    page: int | None = None
    per_page: int | None = None
    state: str | None = None

@dataclass
class PackagesDeletePackageVersionForOrgParams:
    """Parameters for packages_delete_package_version_for_org."""
    package_type: str
    package_name: str
    org: str
    package_version_id: int

@dataclass
class PackagesGetPackageVersionForOrganizationParams:
    """Parameters for packages_get_package_version_for_organization."""
    package_type: str
    package_name: str
    org: str
    package_version_id: int

@dataclass
class PackagesRestorePackageVersionForOrgParams:
    """Parameters for packages_restore_package_version_for_org."""
    package_type: str
    package_name: str
    org: str
    package_version_id: int

@dataclass
class OrgsReviewPatGrantRequestsInBulkParams:
    """Parameters for orgs_review_pat_grant_requests_in_bulk."""
    org: str
    pat_request_ids: list | None = None
    action: str
    reason: str | None = None

@dataclass
class OrgsListPatGrantRequestsParams:
    """Parameters for orgs_list_pat_grant_requests."""
    org: str
    per_page: int | None = None
    page: int | None = None
    sort: str | None = None
    direction: str | None = None
    owner: list | None = None
    repository: str | None = None
    permission: str | None = None
    last_used_before: str | None = None
    last_used_after: str | None = None
    token_id: list | None = None

@dataclass
class OrgsReviewPatGrantRequestParams:
    """Parameters for orgs_review_pat_grant_request."""
    org: str
    pat_request_id: int
    action: str
    reason: str | None = None

@dataclass
class OrgsListPatGrantRequestRepositoriesParams:
    """Parameters for orgs_list_pat_grant_request_repositories."""
    org: str
    pat_request_id: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class OrgsUpdatePatAccessesParams:
    """Parameters for orgs_update_pat_accesses."""
    org: str
    action: str
    pat_ids: list

@dataclass
class OrgsListPatGrantsParams:
    """Parameters for orgs_list_pat_grants."""
    org: str
    per_page: int | None = None
    page: int | None = None
    sort: str | None = None
    direction: str | None = None
    owner: list | None = None
    repository: str | None = None
    permission: str | None = None
    last_used_before: str | None = None
    last_used_after: str | None = None
    token_id: list | None = None

@dataclass
class OrgsUpdatePatAccessParams:
    """Parameters for orgs_update_pat_access."""
    org: str
    pat_id: int
    action: str

@dataclass
class OrgsListPatGrantRepositoriesParams:
    """Parameters for orgs_list_pat_grant_repositories."""
    org: str
    pat_id: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class PrivateRegistriesCreateOrgPrivateRegistryParams:
    """Parameters for private_registries_create_org_private_registry."""
    org: str
    registry_type: str
    url: str
    username: str | None = None
    replaces_base: bool | None = None
    encrypted_value: str
    key_id: str
    visibility: str
    selected_repository_ids: list | None = None

@dataclass
class PrivateRegistriesListOrgPrivateRegistriesParams:
    """Parameters for private_registries_list_org_private_registries."""
    org: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class PrivateRegistriesGetOrgPublicKeyParams:
    """Parameters for private_registries_get_org_public_key."""
    org: str

@dataclass
class PrivateRegistriesUpdateOrgPrivateRegistryParams:
    """Parameters for private_registries_update_org_private_registry."""
    org: str
    secret_name: str
    registry_type: str | None = None
    url: str | None = None
    username: str | None = None
    replaces_base: bool | None = None
    encrypted_value: str | None = None
    key_id: str | None = None
    visibility: str | None = None
    selected_repository_ids: list | None = None

@dataclass
class PrivateRegistriesDeleteOrgPrivateRegistryParams:
    """Parameters for private_registries_delete_org_private_registry."""
    org: str
    secret_name: str

@dataclass
class PrivateRegistriesGetOrgPrivateRegistryParams:
    """Parameters for private_registries_get_org_private_registry."""
    org: str
    secret_name: str

@dataclass
class ProjectsListForOrgParams:
    """Parameters for projects_list_for_org."""
    org: str
    q: str | None = None
    before: str | None = None
    after: str | None = None
    per_page: int | None = None

@dataclass
class ProjectsGetForOrgParams:
    """Parameters for projects_get_for_org."""
    project_number: int
    org: str

@dataclass
class ProjectsCreateDraftItemForOrgParams:
    """Parameters for projects_create_draft_item_for_org."""
    org: str
    project_number: int
    title: str
    body: str | None = None

@dataclass
class ProjectsAddFieldForOrgParams:
    """Parameters for projects_add_field_for_org."""
    project_number: int
    org: str
    body: dict

@dataclass
class ProjectsListFieldsForOrgParams:
    """Parameters for projects_list_fields_for_org."""
    project_number: int
    org: str
    per_page: int | None = None
    before: str | None = None
    after: str | None = None

@dataclass
class ProjectsGetFieldForOrgParams:
    """Parameters for projects_get_field_for_org."""
    project_number: int
    field_id: int
    org: str

@dataclass
class ProjectsAddItemForOrgParams:
    """Parameters for projects_add_item_for_org."""
    org: str
    project_number: int
    type: str
    id: int | None = None
    owner: str | None = None
    repo: str | None = None
    number: int | None = None

@dataclass
class ProjectsListItemsForOrgParams:
    """Parameters for projects_list_items_for_org."""
    project_number: int
    org: str
    q: str | None = None
    fields: dict | None = None
    before: str | None = None
    after: str | None = None
    per_page: int | None = None

@dataclass
class ProjectsUpdateItemForOrgParams:
    """Parameters for projects_update_item_for_org."""
    project_number: int
    org: str
    item_id: int
    fields: list

@dataclass
class ProjectsDeleteItemForOrgParams:
    """Parameters for projects_delete_item_for_org."""
    project_number: int
    org: str
    item_id: int

@dataclass
class ProjectsGetOrgItemParams:
    """Parameters for projects_get_org_item."""
    project_number: int
    org: str
    item_id: int
    fields: dict | None = None

@dataclass
class ProjectsCreateViewForOrgParams:
    """Parameters for projects_create_view_for_org."""
    org: str
    project_number: int
    name: str
    layout: str
    filter: str | None = None
    visible_fields: list | None = None

@dataclass
class ProjectsListViewItemsForOrgParams:
    """Parameters for projects_list_view_items_for_org."""
    project_number: int
    org: str
    view_number: int
    fields: dict | None = None
    before: str | None = None
    after: str | None = None
    per_page: int | None = None

@dataclass
class PatchOrgsByOrgPropertiesSchemaParams:
    """Parameters for patch_orgs_by_org_properties_schema."""
    org: str
    properties: list

@dataclass
class GetOrgsByOrgPropertiesSchemaParams:
    """Parameters for get_orgs_by_org_properties_schema."""
    org: str

@dataclass
class DeleteOrgsByOrgPropertiesSchemaByCustomPropertyNameParams:
    """Parameters for delete_orgs_by_org_properties_schema_by_custom_property_name."""
    org: str
    custom_property_name: str

@dataclass
class PutOrgsByOrgPropertiesSchemaByCustomPropertyNameParams:
    """Parameters for put_orgs_by_org_properties_schema_by_custom_property_name."""
    org: str
    custom_property_name: str
    value_type: str
    required: bool | None = None
    default_value: dict | None = None
    description: str | None = None
    allowed_values: list | None = None
    values_editable_by: str | None = None
    require_explicit_values: bool | None = None

@dataclass
class GetOrgsByOrgPropertiesSchemaByCustomPropertyNameParams:
    """Parameters for get_orgs_by_org_properties_schema_by_custom_property_name."""
    org: str
    custom_property_name: str

@dataclass
class PatchOrgsByOrgPropertiesValuesParams:
    """Parameters for patch_orgs_by_org_properties_values."""
    org: str
    repository_names: list
    properties: list

@dataclass
class GetOrgsByOrgPropertiesValuesParams:
    """Parameters for get_orgs_by_org_properties_values."""
    org: str
    per_page: int | None = None
    page: int | None = None
    repository_query: str | None = None

@dataclass
class OrgsListPublicMembersParams:
    """Parameters for orgs_list_public_members."""
    org: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class DeleteOrgsByOrgPublicMembersByUsernameParams:
    """Parameters for delete_orgs_by_org_public_members_by_username."""
    org: str
    username: str

@dataclass
class OrgsSetPublicMembershipForAuthenticatedUserParams:
    """Parameters for orgs_set_public_membership_for_authenticated_user."""
    org: str
    username: str

@dataclass
class OrgsCheckPublicMembershipForUserParams:
    """Parameters for orgs_check_public_membership_for_user."""
    org: str
    username: str

@dataclass
class ReposCreateInOrgParams:
    """Parameters for repos_create_in_org."""
    org: str
    name: str
    description: str | None = None
    homepage: str | None = None
    private: bool | None = None
    visibility: str | None = None
    has_issues: bool | None = None
    has_projects: bool | None = None
    has_wiki: bool | None = None
    has_downloads: bool | None = None
    is_template: bool | None = None
    team_id: int | None = None
    auto_init: bool | None = None
    gitignore_template: str | None = None
    license_template: str | None = None
    allow_squash_merge: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_auto_merge: bool | None = None
    delete_branch_on_merge: bool | None = None
    use_squash_pr_title_as_default: bool | None = None
    squash_merge_commit_title: str | None = None
    squash_merge_commit_message: str | None = None
    merge_commit_title: str | None = None
    merge_commit_message: str | None = None
    custom_properties: dict | None = None

@dataclass
class ReposListForOrgParams:
    """Parameters for repos_list_for_org."""
    org: str
    type: str | None = None
    sort: str | None = None
    direction: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposCreateOrgRulesetParams:
    """Parameters for repos_create_org_ruleset."""
    org: str
    name: str
    target: str | None = None
    enforcement: str
    bypass_actors: list | None = None
    conditions: dict | None = None
    rules: list | None = None

@dataclass
class ReposGetOrgRulesetsParams:
    """Parameters for repos_get_org_rulesets."""
    org: str
    per_page: int | None = None
    page: int | None = None
    targets: str | None = None

@dataclass
class ReposGetOrgRuleSuitesParams:
    """Parameters for repos_get_org_rule_suites."""
    org: str
    ref: str | None = None
    repository_name: str | None = None
    time_period: str | None = None
    actor_name: str | None = None
    rule_suite_result: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposGetOrgRuleSuiteParams:
    """Parameters for repos_get_org_rule_suite."""
    org: str
    rule_suite_id: int

@dataclass
class ReposDeleteOrgRulesetParams:
    """Parameters for repos_delete_org_ruleset."""
    org: str
    ruleset_id: int

@dataclass
class ReposUpdateOrgRulesetParams:
    """Parameters for repos_update_org_ruleset."""
    org: str
    ruleset_id: int
    name: str | None = None
    target: str | None = None
    enforcement: str | None = None
    bypass_actors: list | None = None
    conditions: dict | None = None
    rules: list | None = None

@dataclass
class ReposGetOrgRulesetParams:
    """Parameters for repos_get_org_ruleset."""
    org: str
    ruleset_id: int

@dataclass
class OrgsGetOrgRulesetHistoryParams:
    """Parameters for orgs_get_org_ruleset_history."""
    org: str
    per_page: int | None = None
    page: int | None = None
    ruleset_id: int

@dataclass
class OrgsGetOrgRulesetVersionParams:
    """Parameters for orgs_get_org_ruleset_version."""
    org: str
    ruleset_id: int
    version_id: int

@dataclass
class SecretScanningListAlertsForOrgParams:
    """Parameters for secret_scanning_list_alerts_for_org."""
    org: str
    state: str | None = None
    secret_type: str | None = None
    resolution: str | None = None
    assignee: str | None = None
    sort: str | None = None
    direction: str | None = None
    page: int | None = None
    per_page: int | None = None
    before: str | None = None
    after: str | None = None
    validity: str | None = None
    is_publicly_leaked: bool | None = None
    is_multi_repo: bool | None = None
    hide_secret: bool | None = None

@dataclass
class SecretScanningUpdateOrgPatternConfigsParams:
    """Parameters for secret_scanning_update_org_pattern_configs."""
    org: str
    pattern_config_version: str | None = None
    provider_pattern_settings: list | None = None
    custom_pattern_settings: list | None = None

@dataclass
class SecretScanningListOrgPatternConfigsParams:
    """Parameters for secret_scanning_list_org_pattern_configs."""
    org: str

@dataclass
class GetOrgsByOrgSecurityAdvisoriesParams:
    """Parameters for get_orgs_by_org_security_advisories."""
    org: str
    direction: str | None = None
    sort: str | None = None
    before: str | None = None
    after: str | None = None
    per_page: int | None = None
    state: str | None = None

@dataclass
class OrgsListSecurityManagerTeamsParams:
    """Parameters for orgs_list_security_manager_teams."""
    org: str

@dataclass
class OrgsRemoveSecurityManagerTeamParams:
    """Parameters for orgs_remove_security_manager_team."""
    org: str
    team_slug: str

@dataclass
class OrgsAddSecurityManagerTeamParams:
    """Parameters for orgs_add_security_manager_team."""
    org: str
    team_slug: str

@dataclass
class OrgsSetImmutableReleasesSettingsParams:
    """Parameters for orgs_set_immutable_releases_settings."""
    org: str
    enforced_repositories: str
    selected_repository_ids: list | None = None

@dataclass
class OrgsGetImmutableReleasesSettingsParams:
    """Parameters for orgs_get_immutable_releases_settings."""
    org: str

@dataclass
class OrgsSetImmutableReleasesSettingsRepositoriesParams:
    """Parameters for orgs_set_immutable_releases_settings_repositories."""
    org: str
    selected_repository_ids: list

@dataclass
class OrgsGetImmutableReleasesSettingsRepositoriesParams:
    """Parameters for orgs_get_immutable_releases_settings_repositories."""
    org: str
    page: int | None = None
    per_page: int | None = None

@dataclass
class DeleteOrgsByOrgSettingsImmutableReleasesRepositoriesByRepositoryIdParams:
    """Parameters for delete_orgs_by_org_settings_immutable_releases_repositories_by_repository_id."""
    org: str
    repository_id: int

@dataclass
class PutOrgsByOrgSettingsImmutableReleasesRepositoriesByRepositoryIdParams:
    """Parameters for put_orgs_by_org_settings_immutable_releases_repositories_by_repository_id."""
    org: str
    repository_id: int

@dataclass
class PostOrgsByOrgSettingsNetworkConfigurationsParams:
    """Parameters for post_orgs_by_org_settings_network_configurations."""
    org: str
    name: str
    compute_service: str | None = None
    network_settings_ids: list

@dataclass
class GetOrgsByOrgSettingsNetworkConfigurationsParams:
    """Parameters for get_orgs_by_org_settings_network_configurations."""
    org: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class PatchOrgsByOrgSettingsNetworkConfigurationsByNetworkConfigurationIdParams:
    """Parameters for patch_orgs_by_org_settings_network_configurations_by_network_configuration_id."""
    org: str
    network_configuration_id: str
    name: str | None = None
    compute_service: str | None = None
    network_settings_ids: list | None = None

@dataclass
class DeleteOrgsByOrgSettingsNetworkConfigurationsByNetworkConfigurationIdParams:
    """Parameters for delete_orgs_by_org_settings_network_configurations_by_network_configuration_id."""
    org: str
    network_configuration_id: str

@dataclass
class HostedComputeGetNetworkConfigurationForOrgParams:
    """Parameters for hosted_compute_get_network_configuration_for_org."""
    org: str
    network_configuration_id: str

@dataclass
class HostedComputeGetNetworkSettingsForOrgParams:
    """Parameters for hosted_compute_get_network_settings_for_org."""
    org: str
    network_settings_id: str

@dataclass
class CopilotCopilotMetricsForTeamParams:
    """Parameters for copilot_copilot_metrics_for_team."""
    org: str
    team_slug: str
    since: str | None = None
    until: str | None = None
    page: int | None = None
    per_page: int | None = None

@dataclass
class TeamsCreateParams:
    """Parameters for teams_create."""
    org: str
    name: str
    description: str | None = None
    maintainers: list | None = None
    repo_names: list | None = None
    privacy: str | None = None
    notification_setting: str | None = None
    permission: str | None = None
    parent_team_id: int | None = None

@dataclass
class TeamsListParams:
    """Parameters for teams_list."""
    org: str
    per_page: int | None = None
    page: int | None = None
    team_type: str | None = None

@dataclass
class TeamsUpdateInOrgParams:
    """Parameters for teams_update_in_org."""
    org: str
    team_slug: str
    name: str | None = None
    description: str | None = None
    privacy: str | None = None
    notification_setting: str | None = None
    permission: str | None = None
    parent_team_id: int | None = None

@dataclass
class TeamsDeleteInOrgParams:
    """Parameters for teams_delete_in_org."""
    org: str
    team_slug: str

@dataclass
class TeamsGetByNameParams:
    """Parameters for teams_get_by_name."""
    org: str
    team_slug: str

@dataclass
class TeamsListPendingInvitationsInOrgParams:
    """Parameters for teams_list_pending_invitations_in_org."""
    org: str
    team_slug: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class TeamsListMembersInOrgParams:
    """Parameters for teams_list_members_in_org."""
    org: str
    team_slug: str
    role: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class TeamsRemoveMembershipForUserInOrgParams:
    """Parameters for teams_remove_membership_for_user_in_org."""
    org: str
    team_slug: str
    username: str

@dataclass
class TeamsAddOrUpdateMembershipForUserInOrgParams:
    """Parameters for teams_add_or_update_membership_for_user_in_org."""
    org: str
    team_slug: str
    username: str
    role: str | None = None

@dataclass
class TeamsGetMembershipForUserInOrgParams:
    """Parameters for teams_get_membership_for_user_in_org."""
    org: str
    team_slug: str
    username: str

@dataclass
class TeamsListReposInOrgParams:
    """Parameters for teams_list_repos_in_org."""
    org: str
    team_slug: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class TeamsRemoveRepoInOrgParams:
    """Parameters for teams_remove_repo_in_org."""
    org: str
    team_slug: str
    owner: str
    repo: str

@dataclass
class TeamsAddOrUpdateRepoPermissionsInOrgParams:
    """Parameters for teams_add_or_update_repo_permissions_in_org."""
    org: str
    team_slug: str
    owner: str
    repo: str
    permission: str | None = None

@dataclass
class TeamsCheckPermissionsForRepoInOrgParams:
    """Parameters for teams_check_permissions_for_repo_in_org."""
    org: str
    team_slug: str
    owner: str
    repo: str

@dataclass
class TeamsListChildInOrgParams:
    """Parameters for teams_list_child_in_org."""
    org: str
    team_slug: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class PostOrgsByOrgBySecurityProductByEnablementParams:
    """Parameters for post_orgs_by_org_by_security_product_by_enablement."""
    org: str
    security_product: str
    enablement: str
    body: dict | None = None

@dataclass
class ReposUpdateParams:
    """Parameters for repos_update."""
    owner: str
    repo: str
    name: str | None = None
    description: str | None = None
    homepage: str | None = None
    private: bool | None = None
    visibility: str | None = None
    security_and_analysis: dict | None = None
    has_issues: bool | None = None
    has_projects: bool | None = None
    has_wiki: bool | None = None
    is_template: bool | None = None
    default_branch: str | None = None
    allow_squash_merge: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_auto_merge: bool | None = None
    delete_branch_on_merge: bool | None = None
    allow_update_branch: bool | None = None
    use_squash_pr_title_as_default: bool | None = None
    squash_merge_commit_title: str | None = None
    squash_merge_commit_message: str | None = None
    merge_commit_title: str | None = None
    merge_commit_message: str | None = None
    archived: bool | None = None
    allow_forking: bool | None = None
    web_commit_signoff_required: bool | None = None

@dataclass
class ReposDeleteParams:
    """Parameters for repos_delete."""
    owner: str
    repo: str

@dataclass
class ReposGetParams:
    """Parameters for repos_get."""
    owner: str
    repo: str

@dataclass
class ActionsListArtifactsForRepoParams:
    """Parameters for actions_list_artifacts_for_repo."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None
    name: str | None = None

@dataclass
class ActionsDeleteArtifactParams:
    """Parameters for actions_delete_artifact."""
    owner: str
    repo: str
    artifact_id: int

@dataclass
class ActionsGetArtifactParams:
    """Parameters for actions_get_artifact."""
    owner: str
    repo: str
    artifact_id: int

@dataclass
class ActionsDownloadArtifactParams:
    """Parameters for actions_download_artifact."""
    owner: str
    repo: str
    artifact_id: int
    archive_format: str

@dataclass
class PutReposByOwnerByRepoActionsCacheRetentionLimitParams:
    """Parameters for put_repos_by_owner_by_repo_actions_cache_retention_limit."""
    owner: str
    repo: str
    max_cache_retention_days: int | None = None

@dataclass
class GetReposByOwnerByRepoActionsCacheRetentionLimitParams:
    """Parameters for get_repos_by_owner_by_repo_actions_cache_retention_limit."""
    owner: str
    repo: str

@dataclass
class PutReposByOwnerByRepoActionsCacheStorageLimitParams:
    """Parameters for put_repos_by_owner_by_repo_actions_cache_storage_limit."""
    owner: str
    repo: str
    max_cache_size_gb: int | None = None

@dataclass
class GetReposByOwnerByRepoActionsCacheStorageLimitParams:
    """Parameters for get_repos_by_owner_by_repo_actions_cache_storage_limit."""
    owner: str
    repo: str

@dataclass
class ActionsGetActionsCacheUsageParams:
    """Parameters for actions_get_actions_cache_usage."""
    owner: str
    repo: str

@dataclass
class ActionsDeleteActionsCacheByKeyParams:
    """Parameters for actions_delete_actions_cache_by_key."""
    owner: str
    repo: str
    key: str
    ref: str | None = None

@dataclass
class ActionsGetActionsCacheListParams:
    """Parameters for actions_get_actions_cache_list."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None
    ref: str | None = None
    key: str | None = None
    sort: str | None = None
    direction: str | None = None

@dataclass
class ActionsDeleteActionsCacheByIdParams:
    """Parameters for actions_delete_actions_cache_by_id."""
    owner: str
    repo: str
    cache_id: int

@dataclass
class ActionsGetJobForWorkflowRunParams:
    """Parameters for actions_get_job_for_workflow_run."""
    owner: str
    repo: str
    job_id: int

@dataclass
class ActionsDownloadJobLogsForWorkflowRunParams:
    """Parameters for actions_download_job_logs_for_workflow_run."""
    owner: str
    repo: str
    job_id: int

@dataclass
class ActionsReRunJobForWorkflowRunParams:
    """Parameters for actions_re_run_job_for_workflow_run."""
    owner: str
    repo: str
    job_id: int
    enable_debug_logging: bool | None = None

@dataclass
class ActionsSetCustomOidcSubClaimForRepoParams:
    """Parameters for actions_set_custom_oidc_sub_claim_for_repo."""
    owner: str
    repo: str
    use_default: bool
    include_claim_keys: list | None = None

@dataclass
class ActionsGetCustomOidcSubClaimForRepoParams:
    """Parameters for actions_get_custom_oidc_sub_claim_for_repo."""
    owner: str
    repo: str

@dataclass
class ActionsListRepoOrganizationSecretsParams:
    """Parameters for actions_list_repo_organization_secrets."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActionsListRepoOrganizationVariablesParams:
    """Parameters for actions_list_repo_organization_variables."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActionsSetGithubActionsPermissionsRepositoryParams:
    """Parameters for actions_set_github_actions_permissions_repository."""
    owner: str
    repo: str
    enabled: bool
    allowed_actions: str | None = None
    sha_pinning_required: bool | None = None

@dataclass
class ActionsGetGithubActionsPermissionsRepositoryParams:
    """Parameters for actions_get_github_actions_permissions_repository."""
    owner: str
    repo: str

@dataclass
class ActionsSetWorkflowAccessToRepositoryParams:
    """Parameters for actions_set_workflow_access_to_repository."""
    owner: str
    repo: str
    access_level: str

@dataclass
class ActionsGetWorkflowAccessToRepositoryParams:
    """Parameters for actions_get_workflow_access_to_repository."""
    owner: str
    repo: str

@dataclass
class PutReposByOwnerByRepoActionsPermissionsArtifactAndLogRetentionParams:
    """Parameters for put_repos_by_owner_by_repo_actions_permissions_artifact_and_log_retention."""
    owner: str
    repo: str
    days: int

@dataclass
class GetReposByOwnerByRepoActionsPermissionsArtifactAndLogRetentionParams:
    """Parameters for get_repos_by_owner_by_repo_actions_permissions_artifact_and_log_retention."""
    owner: str
    repo: str

@dataclass
class PutReposByOwnerByRepoActionsPermissionsForkPrContributorApprovalParams:
    """Parameters for put_repos_by_owner_by_repo_actions_permissions_fork_pr_contributor_approval."""
    owner: str
    repo: str
    approval_policy: str

@dataclass
class GetReposByOwnerByRepoActionsPermissionsForkPrContributorApprovalParams:
    """Parameters for get_repos_by_owner_by_repo_actions_permissions_fork_pr_contributor_approval."""
    owner: str
    repo: str

@dataclass
class PutReposByOwnerByRepoActionsPermissionsForkPrWorkflowsPrivateReposParams:
    """Parameters for put_repos_by_owner_by_repo_actions_permissions_fork_pr_workflows_private_repos."""
    owner: str
    repo: str
    run_workflows_from_fork_pull_requests: bool
    send_write_tokens_to_workflows: bool | None = None
    send_secrets_and_variables: bool | None = None
    require_approval_for_fork_pr_workflows: bool | None = None

@dataclass
class GetReposByOwnerByRepoActionsPermissionsForkPrWorkflowsPrivateReposParams:
    """Parameters for get_repos_by_owner_by_repo_actions_permissions_fork_pr_workflows_private_repos."""
    owner: str
    repo: str

@dataclass
class ActionsSetAllowedActionsRepositoryParams:
    """Parameters for actions_set_allowed_actions_repository."""
    owner: str
    repo: str
    github_owned_allowed: bool | None = None
    verified_allowed: bool | None = None
    patterns_allowed: list | None = None

@dataclass
class ActionsGetAllowedActionsRepositoryParams:
    """Parameters for actions_get_allowed_actions_repository."""
    owner: str
    repo: str

@dataclass
class PutReposByOwnerByRepoActionsPermissionsWorkflowParams:
    """Parameters for put_repos_by_owner_by_repo_actions_permissions_workflow."""
    owner: str
    repo: str
    default_workflow_permissions: str | None = None
    can_approve_pull_request_reviews: bool | None = None

@dataclass
class GetReposByOwnerByRepoActionsPermissionsWorkflowParams:
    """Parameters for get_repos_by_owner_by_repo_actions_permissions_workflow."""
    owner: str
    repo: str

@dataclass
class ActionsListSelfHostedRunnersForRepoParams:
    """Parameters for actions_list_self_hosted_runners_for_repo."""
    name: str | None = None
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActionsListRunnerApplicationsForRepoParams:
    """Parameters for actions_list_runner_applications_for_repo."""
    owner: str
    repo: str

@dataclass
class ActionsGenerateRunnerJitconfigForRepoParams:
    """Parameters for actions_generate_runner_jitconfig_for_repo."""
    owner: str
    repo: str
    name: str
    runner_group_id: int
    labels: list
    work_folder: str | None = None

@dataclass
class ActionsCreateRegistrationTokenForRepoParams:
    """Parameters for actions_create_registration_token_for_repo."""
    owner: str
    repo: str

@dataclass
class ActionsCreateRemoveTokenForRepoParams:
    """Parameters for actions_create_remove_token_for_repo."""
    owner: str
    repo: str

@dataclass
class ActionsDeleteSelfHostedRunnerFromRepoParams:
    """Parameters for actions_delete_self_hosted_runner_from_repo."""
    owner: str
    repo: str
    runner_id: int

@dataclass
class ActionsGetSelfHostedRunnerForRepoParams:
    """Parameters for actions_get_self_hosted_runner_for_repo."""
    owner: str
    repo: str
    runner_id: int

@dataclass
class PostReposByOwnerByRepoActionsRunnersByRunnerIdLabelsParams:
    """Parameters for post_repos_by_owner_by_repo_actions_runners_by_runner_id_labels."""
    owner: str
    repo: str
    runner_id: int
    labels: list

@dataclass
class DeleteReposByOwnerByRepoActionsRunnersByRunnerIdLabelsParams:
    """Parameters for delete_repos_by_owner_by_repo_actions_runners_by_runner_id_labels."""
    owner: str
    repo: str
    runner_id: int

@dataclass
class PutReposByOwnerByRepoActionsRunnersByRunnerIdLabelsParams:
    """Parameters for put_repos_by_owner_by_repo_actions_runners_by_runner_id_labels."""
    owner: str
    repo: str
    runner_id: int
    labels: list

@dataclass
class GetReposByOwnerByRepoActionsRunnersByRunnerIdLabelsParams:
    """Parameters for get_repos_by_owner_by_repo_actions_runners_by_runner_id_labels."""
    owner: str
    repo: str
    runner_id: int

@dataclass
class DeleteReposByOwnerByRepoActionsRunnersByRunnerIdLabelsByNameParams:
    """Parameters for delete_repos_by_owner_by_repo_actions_runners_by_runner_id_labels_by_name."""
    owner: str
    repo: str
    runner_id: int
    name: str

@dataclass
class ActionsListWorkflowRunsForRepoParams:
    """Parameters for actions_list_workflow_runs_for_repo."""
    owner: str
    repo: str
    actor: str | None = None
    branch: str | None = None
    event: str | None = None
    status: str | None = None
    per_page: int | None = None
    page: int | None = None
    created: str | None = None
    exclude_pull_requests: bool | None = None
    check_suite_id: int | None = None
    head_sha: str | None = None

@dataclass
class ActionsDeleteWorkflowRunParams:
    """Parameters for actions_delete_workflow_run."""
    owner: str
    repo: str
    run_id: int

@dataclass
class ActionsGetWorkflowRunParams:
    """Parameters for actions_get_workflow_run."""
    owner: str
    repo: str
    run_id: int
    exclude_pull_requests: bool | None = None

@dataclass
class ActionsGetReviewsForRunParams:
    """Parameters for actions_get_reviews_for_run."""
    owner: str
    repo: str
    run_id: int

@dataclass
class ActionsApproveWorkflowRunParams:
    """Parameters for actions_approve_workflow_run."""
    owner: str
    repo: str
    run_id: int

@dataclass
class ActionsListWorkflowRunArtifactsParams:
    """Parameters for actions_list_workflow_run_artifacts."""
    owner: str
    repo: str
    run_id: int
    per_page: int | None = None
    page: int | None = None
    name: str | None = None
    direction: str | None = None

@dataclass
class ActionsGetWorkflowRunAttemptParams:
    """Parameters for actions_get_workflow_run_attempt."""
    owner: str
    repo: str
    run_id: int
    attempt_number: int
    exclude_pull_requests: bool | None = None

@dataclass
class ActionsListJobsForWorkflowRunAttemptParams:
    """Parameters for actions_list_jobs_for_workflow_run_attempt."""
    owner: str
    repo: str
    run_id: int
    attempt_number: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActionsDownloadWorkflowRunAttemptLogsParams:
    """Parameters for actions_download_workflow_run_attempt_logs."""
    owner: str
    repo: str
    run_id: int
    attempt_number: int

@dataclass
class ActionsCancelWorkflowRunParams:
    """Parameters for actions_cancel_workflow_run."""
    owner: str
    repo: str
    run_id: int

@dataclass
class ActionsReviewCustomGatesForRunParams:
    """Parameters for actions_review_custom_gates_for_run."""
    owner: str
    repo: str
    run_id: int
    body: dict

@dataclass
class ActionsForceCancelWorkflowRunParams:
    """Parameters for actions_force_cancel_workflow_run."""
    owner: str
    repo: str
    run_id: int

@dataclass
class ActionsListJobsForWorkflowRunParams:
    """Parameters for actions_list_jobs_for_workflow_run."""
    owner: str
    repo: str
    run_id: int
    filter: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActionsDeleteWorkflowRunLogsParams:
    """Parameters for actions_delete_workflow_run_logs."""
    owner: str
    repo: str
    run_id: int

@dataclass
class ActionsDownloadWorkflowRunLogsParams:
    """Parameters for actions_download_workflow_run_logs."""
    owner: str
    repo: str
    run_id: int

@dataclass
class ActionsReviewPendingDeploymentsForRunParams:
    """Parameters for actions_review_pending_deployments_for_run."""
    owner: str
    repo: str
    run_id: int
    environment_ids: list
    state: str
    comment: str

@dataclass
class ActionsGetPendingDeploymentsForRunParams:
    """Parameters for actions_get_pending_deployments_for_run."""
    owner: str
    repo: str
    run_id: int

@dataclass
class ActionsReRunWorkflowParams:
    """Parameters for actions_re_run_workflow."""
    owner: str
    repo: str
    run_id: int
    enable_debug_logging: bool | None = None

@dataclass
class ActionsReRunWorkflowFailedJobsParams:
    """Parameters for actions_re_run_workflow_failed_jobs."""
    owner: str
    repo: str
    run_id: int
    enable_debug_logging: bool | None = None

@dataclass
class ActionsGetWorkflowRunUsageParams:
    """Parameters for actions_get_workflow_run_usage."""
    owner: str
    repo: str
    run_id: int

@dataclass
class ActionsListRepoSecretsParams:
    """Parameters for actions_list_repo_secrets."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActionsGetRepoPublicKeyParams:
    """Parameters for actions_get_repo_public_key."""
    owner: str
    repo: str

@dataclass
class ActionsDeleteRepoSecretParams:
    """Parameters for actions_delete_repo_secret."""
    owner: str
    repo: str
    secret_name: str

@dataclass
class ActionsCreateOrUpdateRepoSecretParams:
    """Parameters for actions_create_or_update_repo_secret."""
    owner: str
    repo: str
    secret_name: str
    encrypted_value: str
    key_id: str

@dataclass
class ActionsGetRepoSecretParams:
    """Parameters for actions_get_repo_secret."""
    owner: str
    repo: str
    secret_name: str

@dataclass
class ActionsCreateRepoVariableParams:
    """Parameters for actions_create_repo_variable."""
    owner: str
    repo: str
    name: str
    value: str

@dataclass
class ActionsListRepoVariablesParams:
    """Parameters for actions_list_repo_variables."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActionsUpdateRepoVariableParams:
    """Parameters for actions_update_repo_variable."""
    owner: str
    repo: str
    name: str
    value: str | None = None

@dataclass
class ActionsDeleteRepoVariableParams:
    """Parameters for actions_delete_repo_variable."""
    owner: str
    repo: str
    name: str

@dataclass
class ActionsGetRepoVariableParams:
    """Parameters for actions_get_repo_variable."""
    owner: str
    repo: str
    name: str

@dataclass
class ActionsListRepoWorkflowsParams:
    """Parameters for actions_list_repo_workflows."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActionsGetWorkflowParams:
    """Parameters for actions_get_workflow."""
    owner: str
    repo: str
    workflow_id: dict

@dataclass
class ActionsDisableWorkflowParams:
    """Parameters for actions_disable_workflow."""
    owner: str
    repo: str
    workflow_id: dict

@dataclass
class ActionsCreateWorkflowDispatchParams:
    """Parameters for actions_create_workflow_dispatch."""
    owner: str
    repo: str
    workflow_id: dict
    ref: str
    inputs: dict | None = None
    return_run_details: bool | None = None

@dataclass
class ActionsEnableWorkflowParams:
    """Parameters for actions_enable_workflow."""
    owner: str
    repo: str
    workflow_id: dict

@dataclass
class ActionsListWorkflowRunsParams:
    """Parameters for actions_list_workflow_runs."""
    owner: str
    repo: str
    workflow_id: dict
    actor: str | None = None
    branch: str | None = None
    event: str | None = None
    status: str | None = None
    per_page: int | None = None
    page: int | None = None
    created: str | None = None
    exclude_pull_requests: bool | None = None
    check_suite_id: int | None = None
    head_sha: str | None = None

@dataclass
class ActionsGetWorkflowUsageParams:
    """Parameters for actions_get_workflow_usage."""
    owner: str
    repo: str
    workflow_id: dict

@dataclass
class ReposListActivitiesParams:
    """Parameters for repos_list_activities."""
    owner: str
    repo: str
    direction: str | None = None
    per_page: int | None = None
    before: str | None = None
    after: str | None = None
    ref: str | None = None
    actor: str | None = None
    time_period: str | None = None
    activity_type: str | None = None

@dataclass
class IssuesListAssigneesParams:
    """Parameters for issues_list_assignees."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class IssuesCheckUserCanBeAssignedParams:
    """Parameters for issues_check_user_can_be_assigned."""
    owner: str
    repo: str
    assignee: str

@dataclass
class ReposCreateAttestationParams:
    """Parameters for repos_create_attestation."""
    owner: str
    repo: str
    bundle: dict

@dataclass
class ReposListAttestationsParams:
    """Parameters for repos_list_attestations."""
    owner: str
    repo: str
    per_page: int | None = None
    before: str | None = None
    after: str | None = None
    subject_digest: str
    predicate_type: str | None = None

@dataclass
class ReposCreateAutolinkParams:
    """Parameters for repos_create_autolink."""
    owner: str
    repo: str
    key_prefix: str
    url_template: str
    is_alphanumeric: bool | None = None

@dataclass
class ReposListAutolinksParams:
    """Parameters for repos_list_autolinks."""
    owner: str
    repo: str

@dataclass
class ReposDeleteAutolinkParams:
    """Parameters for repos_delete_autolink."""
    owner: str
    repo: str
    autolink_id: int

@dataclass
class ReposGetAutolinkParams:
    """Parameters for repos_get_autolink."""
    owner: str
    repo: str
    autolink_id: int

@dataclass
class ReposDisableAutomatedSecurityFixesParams:
    """Parameters for repos_disable_automated_security_fixes."""
    owner: str
    repo: str

@dataclass
class ReposEnableAutomatedSecurityFixesParams:
    """Parameters for repos_enable_automated_security_fixes."""
    owner: str
    repo: str

@dataclass
class ReposCheckAutomatedSecurityFixesParams:
    """Parameters for repos_check_automated_security_fixes."""
    owner: str
    repo: str

@dataclass
class ReposListBranchesParams:
    """Parameters for repos_list_branches."""
    owner: str
    repo: str
    protected: bool | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposGetBranchParams:
    """Parameters for repos_get_branch."""
    owner: str
    repo: str
    branch: str

@dataclass
class ReposDeleteBranchProtectionParams:
    """Parameters for repos_delete_branch_protection."""
    owner: str
    repo: str
    branch: str

@dataclass
class ReposUpdateBranchProtectionParams:
    """Parameters for repos_update_branch_protection."""
    owner: str
    repo: str
    branch: str
    required_status_checks: dict
    enforce_admins: bool
    required_pull_request_reviews: dict
    restrictions: dict
    required_linear_history: bool | None = None
    allow_force_pushes: bool | None = None
    allow_deletions: bool | None = None
    block_creations: bool | None = None
    required_conversation_resolution: bool | None = None
    lock_branch: bool | None = None
    allow_fork_syncing: bool | None = None

@dataclass
class ReposGetBranchProtectionParams:
    """Parameters for repos_get_branch_protection."""
    owner: str
    repo: str
    branch: str

@dataclass
class ReposSetAdminBranchProtectionParams:
    """Parameters for repos_set_admin_branch_protection."""
    owner: str
    repo: str
    branch: str

@dataclass
class ReposDeleteAdminBranchProtectionParams:
    """Parameters for repos_delete_admin_branch_protection."""
    owner: str
    repo: str
    branch: str

@dataclass
class ReposGetAdminBranchProtectionParams:
    """Parameters for repos_get_admin_branch_protection."""
    owner: str
    repo: str
    branch: str

@dataclass
class ReposUpdatePullRequestReviewProtectionParams:
    """Parameters for repos_update_pull_request_review_protection."""
    owner: str
    repo: str
    branch: str
    dismissal_restrictions: dict | None = None
    dismiss_stale_reviews: bool | None = None
    require_code_owner_reviews: bool | None = None
    required_approving_review_count: int | None = None
    require_last_push_approval: bool | None = None
    bypass_pull_request_allowances: dict | None = None

@dataclass
class ReposDeletePullRequestReviewProtectionParams:
    """Parameters for repos_delete_pull_request_review_protection."""
    owner: str
    repo: str
    branch: str

@dataclass
class ReposGetPullRequestReviewProtectionParams:
    """Parameters for repos_get_pull_request_review_protection."""
    owner: str
    repo: str
    branch: str

@dataclass
class ReposCreateCommitSignatureProtectionParams:
    """Parameters for repos_create_commit_signature_protection."""
    owner: str
    repo: str
    branch: str

@dataclass
class ReposDeleteCommitSignatureProtectionParams:
    """Parameters for repos_delete_commit_signature_protection."""
    owner: str
    repo: str
    branch: str

@dataclass
class ReposGetCommitSignatureProtectionParams:
    """Parameters for repos_get_commit_signature_protection."""
    owner: str
    repo: str
    branch: str

@dataclass
class ReposUpdateStatusCheckProtectionParams:
    """Parameters for repos_update_status_check_protection."""
    owner: str
    repo: str
    branch: str
    strict: bool | None = None
    contexts: list | None = None
    checks: list | None = None

@dataclass
class ReposRemoveStatusCheckProtectionParams:
    """Parameters for repos_remove_status_check_protection."""
    owner: str
    repo: str
    branch: str

@dataclass
class ReposGetStatusChecksProtectionParams:
    """Parameters for repos_get_status_checks_protection."""
    owner: str
    repo: str
    branch: str

@dataclass
class ReposAddStatusCheckContextsParams:
    """Parameters for repos_add_status_check_contexts."""
    owner: str
    repo: str
    branch: str
    body: dict | None = None

@dataclass
class ReposRemoveStatusCheckContextsParams:
    """Parameters for repos_remove_status_check_contexts."""
    owner: str
    repo: str
    branch: str
    body: dict

@dataclass
class ReposSetStatusCheckContextsParams:
    """Parameters for repos_set_status_check_contexts."""
    owner: str
    repo: str
    branch: str
    body: dict | None = None

@dataclass
class ReposGetAllStatusCheckContextsParams:
    """Parameters for repos_get_all_status_check_contexts."""
    owner: str
    repo: str
    branch: str

@dataclass
class ReposDeleteAccessRestrictionsParams:
    """Parameters for repos_delete_access_restrictions."""
    owner: str
    repo: str
    branch: str

@dataclass
class ReposGetAccessRestrictionsParams:
    """Parameters for repos_get_access_restrictions."""
    owner: str
    repo: str
    branch: str

@dataclass
class ReposAddAppAccessRestrictionsParams:
    """Parameters for repos_add_app_access_restrictions."""
    owner: str
    repo: str
    branch: str
    apps: list

@dataclass
class ReposRemoveAppAccessRestrictionsParams:
    """Parameters for repos_remove_app_access_restrictions."""
    owner: str
    repo: str
    branch: str
    apps: list

@dataclass
class ReposSetAppAccessRestrictionsParams:
    """Parameters for repos_set_app_access_restrictions."""
    owner: str
    repo: str
    branch: str
    apps: list

@dataclass
class ReposGetAppsWithAccessToProtectedBranchParams:
    """Parameters for repos_get_apps_with_access_to_protected_branch."""
    owner: str
    repo: str
    branch: str

@dataclass
class ReposAddTeamAccessRestrictionsParams:
    """Parameters for repos_add_team_access_restrictions."""
    owner: str
    repo: str
    branch: str
    body: dict | None = None

@dataclass
class ReposRemoveTeamAccessRestrictionsParams:
    """Parameters for repos_remove_team_access_restrictions."""
    owner: str
    repo: str
    branch: str
    body: dict

@dataclass
class ReposSetTeamAccessRestrictionsParams:
    """Parameters for repos_set_team_access_restrictions."""
    owner: str
    repo: str
    branch: str
    body: dict | None = None

@dataclass
class ReposGetTeamsWithAccessToProtectedBranchParams:
    """Parameters for repos_get_teams_with_access_to_protected_branch."""
    owner: str
    repo: str
    branch: str

@dataclass
class ReposAddUserAccessRestrictionsParams:
    """Parameters for repos_add_user_access_restrictions."""
    owner: str
    repo: str
    branch: str
    users: list

@dataclass
class ReposRemoveUserAccessRestrictionsParams:
    """Parameters for repos_remove_user_access_restrictions."""
    owner: str
    repo: str
    branch: str
    users: list

@dataclass
class ReposSetUserAccessRestrictionsParams:
    """Parameters for repos_set_user_access_restrictions."""
    owner: str
    repo: str
    branch: str
    users: list

@dataclass
class ReposGetUsersWithAccessToProtectedBranchParams:
    """Parameters for repos_get_users_with_access_to_protected_branch."""
    owner: str
    repo: str
    branch: str

@dataclass
class ReposRenameBranchParams:
    """Parameters for repos_rename_branch."""
    owner: str
    repo: str
    branch: str
    new_name: str

@dataclass
class ChecksCreateParams:
    """Parameters for checks_create."""
    owner: str
    repo: str
    name: str
    head_sha: str
    details_url: str | None = None
    external_id: str | None = None
    status: str | None = None
    started_at: str | None = None
    conclusion: str | None = None
    completed_at: str | None = None
    output: dict | None = None
    actions: list | None = None

@dataclass
class ChecksUpdateParams:
    """Parameters for checks_update."""
    owner: str
    repo: str
    check_run_id: int
    name: str | None = None
    details_url: str | None = None
    external_id: str | None = None
    started_at: str | None = None
    status: str | None = None
    conclusion: str | None = None
    completed_at: str | None = None
    output: dict | None = None
    actions: list | None = None

@dataclass
class ChecksGetParams:
    """Parameters for checks_get."""
    owner: str
    repo: str
    check_run_id: int

@dataclass
class ChecksListAnnotationsParams:
    """Parameters for checks_list_annotations."""
    owner: str
    repo: str
    check_run_id: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class ChecksRerequestRunParams:
    """Parameters for checks_rerequest_run."""
    owner: str
    repo: str
    check_run_id: int

@dataclass
class ChecksCreateSuiteParams:
    """Parameters for checks_create_suite."""
    owner: str
    repo: str
    head_sha: str

@dataclass
class ChecksSetSuitesPreferencesParams:
    """Parameters for checks_set_suites_preferences."""
    owner: str
    repo: str
    auto_trigger_checks: list | None = None

@dataclass
class ChecksGetSuiteParams:
    """Parameters for checks_get_suite."""
    owner: str
    repo: str
    check_suite_id: int

@dataclass
class ChecksListForSuiteParams:
    """Parameters for checks_list_for_suite."""
    owner: str
    repo: str
    check_suite_id: int
    check_name: str | None = None
    status: str | None = None
    filter: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class ChecksRerequestSuiteParams:
    """Parameters for checks_rerequest_suite."""
    owner: str
    repo: str
    check_suite_id: int

@dataclass
class CodeScanningListAlertsForRepoParams:
    """Parameters for code_scanning_list_alerts_for_repo."""
    owner: str
    repo: str
    tool_name: str | None = None
    tool_guid: str | None = None
    page: int | None = None
    per_page: int | None = None
    ref: str | None = None
    pr: int | None = None
    direction: str | None = None
    before: str | None = None
    after: str | None = None
    sort: str | None = None
    state: str | None = None
    severity: str | None = None
    assignees: str | None = None

@dataclass
class CodeScanningUpdateAlertParams:
    """Parameters for code_scanning_update_alert."""
    owner: str
    repo: str
    alert_number: int
    state: str | None = None
    dismissed_reason: str | None = None
    dismissed_comment: str | None = None
    create_request: bool | None = None
    assignees: list | None = None

@dataclass
class CodeScanningGetAlertParams:
    """Parameters for code_scanning_get_alert."""
    owner: str
    repo: str
    alert_number: int

@dataclass
class CodeScanningCreateAutofixParams:
    """Parameters for code_scanning_create_autofix."""
    owner: str
    repo: str
    alert_number: int

@dataclass
class CodeScanningGetAutofixParams:
    """Parameters for code_scanning_get_autofix."""
    owner: str
    repo: str
    alert_number: int

@dataclass
class CodeScanningCommitAutofixParams:
    """Parameters for code_scanning_commit_autofix."""
    owner: str
    repo: str
    alert_number: int
    target_ref: str | None = None
    message: str | None = None

@dataclass
class CodeScanningListAlertInstancesParams:
    """Parameters for code_scanning_list_alert_instances."""
    owner: str
    repo: str
    alert_number: int
    page: int | None = None
    per_page: int | None = None
    ref: str | None = None
    pr: int | None = None

@dataclass
class CodeScanningListRecentAnalysesParams:
    """Parameters for code_scanning_list_recent_analyses."""
    owner: str
    repo: str
    tool_name: str | None = None
    tool_guid: str | None = None
    page: int | None = None
    per_page: int | None = None
    pr: int | None = None
    ref: str | None = None
    sarif_id: str | None = None
    direction: str | None = None
    sort: str | None = None

@dataclass
class CodeScanningDeleteAnalysisParams:
    """Parameters for code_scanning_delete_analysis."""
    owner: str
    repo: str
    analysis_id: int
    confirm_delete: str | None = None

@dataclass
class CodeScanningGetAnalysisParams:
    """Parameters for code_scanning_get_analysis."""
    owner: str
    repo: str
    analysis_id: int

@dataclass
class CodeScanningListCodeqlDatabasesParams:
    """Parameters for code_scanning_list_codeql_databases."""
    owner: str
    repo: str

@dataclass
class CodeScanningDeleteCodeqlDatabaseParams:
    """Parameters for code_scanning_delete_codeql_database."""
    owner: str
    repo: str
    language: str

@dataclass
class CodeScanningGetCodeqlDatabaseParams:
    """Parameters for code_scanning_get_codeql_database."""
    owner: str
    repo: str
    language: str

@dataclass
class CodeScanningCreateVariantAnalysisParams:
    """Parameters for code_scanning_create_variant_analysis."""
    owner: str
    repo: str
    language: str
    query_pack: str
    repositories: list | None = None
    repository_lists: list | None = None
    repository_owners: list | None = None

@dataclass
class CodeScanningGetVariantAnalysisParams:
    """Parameters for code_scanning_get_variant_analysis."""
    owner: str
    repo: str
    codeql_variant_analysis_id: int

@dataclass
class CodeScanningGetVariantAnalysisRepoTaskParams:
    """Parameters for code_scanning_get_variant_analysis_repo_task."""
    owner: str
    repo: str
    codeql_variant_analysis_id: int
    repo_owner: str
    repo_name: str

@dataclass
class CodeScanningUpdateDefaultSetupParams:
    """Parameters for code_scanning_update_default_setup."""
    owner: str
    repo: str
    state: str | None = None
    runner_type: str | None = None
    runner_label: str | None = None
    query_suite: str | None = None
    threat_model: str | None = None
    languages: list | None = None

@dataclass
class CodeScanningGetDefaultSetupParams:
    """Parameters for code_scanning_get_default_setup."""
    owner: str
    repo: str

@dataclass
class CodeScanningUploadSarifParams:
    """Parameters for code_scanning_upload_sarif."""
    owner: str
    repo: str
    commit_sha: str
    ref: str
    sarif: str
    checkout_uri: str | None = None
    started_at: str | None = None
    tool_name: str | None = None
    validate: bool | None = None

@dataclass
class CodeScanningGetSarifParams:
    """Parameters for code_scanning_get_sarif."""
    owner: str
    repo: str
    sarif_id: str

@dataclass
class CodeSecurityGetConfigurationForRepositoryParams:
    """Parameters for code_security_get_configuration_for_repository."""
    owner: str
    repo: str

@dataclass
class ReposCodeownersErrorsParams:
    """Parameters for repos_codeowners_errors."""
    owner: str
    repo: str
    ref: str | None = None

@dataclass
class PostReposByOwnerByRepoCodespacesParams:
    """Parameters for post_repos_by_owner_by_repo_codespaces."""
    owner: str
    repo: str
    ref: str | None = None
    location: str | None = None
    geo: str | None = None
    client_ip: str | None = None
    machine: str | None = None
    devcontainer_path: str | None = None
    multi_repo_permissions_opt_out: bool | None = None
    working_directory: str | None = None
    idle_timeout_minutes: int | None = None
    display_name: str | None = None
    retention_period_minutes: int | None = None

@dataclass
class GetReposByOwnerByRepoCodespacesParams:
    """Parameters for get_repos_by_owner_by_repo_codespaces."""
    per_page: int | None = None
    page: int | None = None
    owner: str
    repo: str

@dataclass
class GetReposByOwnerByRepoCodespacesDevcontainersParams:
    """Parameters for get_repos_by_owner_by_repo_codespaces_devcontainers."""
    per_page: int | None = None
    page: int | None = None
    owner: str
    repo: str

@dataclass
class CodespacesRepoMachinesForAuthenticatedUserParams:
    """Parameters for codespaces_repo_machines_for_authenticated_user."""
    owner: str
    repo: str
    location: str | None = None
    client_ip: str | None = None
    ref: str | None = None

@dataclass
class GetReposByOwnerByRepoCodespacesNewParams:
    """Parameters for get_repos_by_owner_by_repo_codespaces_new."""
    owner: str
    repo: str
    ref: str | None = None
    client_ip: str | None = None

@dataclass
class CodespacesCheckPermissionsForDevcontainerParams:
    """Parameters for codespaces_check_permissions_for_devcontainer."""
    owner: str
    repo: str
    ref: str
    devcontainer_path: str

@dataclass
class CodespacesListRepoSecretsParams:
    """Parameters for codespaces_list_repo_secrets."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class CodespacesGetRepoPublicKeyParams:
    """Parameters for codespaces_get_repo_public_key."""
    owner: str
    repo: str

@dataclass
class CodespacesDeleteRepoSecretParams:
    """Parameters for codespaces_delete_repo_secret."""
    owner: str
    repo: str
    secret_name: str

@dataclass
class CodespacesCreateOrUpdateRepoSecretParams:
    """Parameters for codespaces_create_or_update_repo_secret."""
    owner: str
    repo: str
    secret_name: str
    encrypted_value: str | None = None
    key_id: str | None = None

@dataclass
class CodespacesGetRepoSecretParams:
    """Parameters for codespaces_get_repo_secret."""
    owner: str
    repo: str
    secret_name: str

@dataclass
class ReposListCollaboratorsParams:
    """Parameters for repos_list_collaborators."""
    owner: str
    repo: str
    affiliation: str | None = None
    permission: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposRemoveCollaboratorParams:
    """Parameters for repos_remove_collaborator."""
    owner: str
    repo: str
    username: str

@dataclass
class ReposAddCollaboratorParams:
    """Parameters for repos_add_collaborator."""
    owner: str
    repo: str
    username: str
    permission: str | None = None

@dataclass
class ReposCheckCollaboratorParams:
    """Parameters for repos_check_collaborator."""
    owner: str
    repo: str
    username: str

@dataclass
class ReposGetCollaboratorPermissionLevelParams:
    """Parameters for repos_get_collaborator_permission_level."""
    owner: str
    repo: str
    username: str

@dataclass
class ReposListCommitCommentsForRepoParams:
    """Parameters for repos_list_commit_comments_for_repo."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposUpdateCommitCommentParams:
    """Parameters for repos_update_commit_comment."""
    owner: str
    repo: str
    comment_id: int
    body: str

@dataclass
class ReposDeleteCommitCommentParams:
    """Parameters for repos_delete_commit_comment."""
    owner: str
    repo: str
    comment_id: int

@dataclass
class ReposGetCommitCommentParams:
    """Parameters for repos_get_commit_comment."""
    owner: str
    repo: str
    comment_id: int

@dataclass
class ReactionsCreateForCommitCommentParams:
    """Parameters for reactions_create_for_commit_comment."""
    owner: str
    repo: str
    comment_id: int
    content: str

@dataclass
class ReactionsListForCommitCommentParams:
    """Parameters for reactions_list_for_commit_comment."""
    owner: str
    repo: str
    comment_id: int
    content: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReactionsDeleteForCommitCommentParams:
    """Parameters for reactions_delete_for_commit_comment."""
    owner: str
    repo: str
    comment_id: int
    reaction_id: int

@dataclass
class ReposListCommitsParams:
    """Parameters for repos_list_commits."""
    owner: str
    repo: str
    sha: str | None = None
    path: str | None = None
    author: str | None = None
    committer: str | None = None
    since: str | None = None
    until: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposListBranchesForHeadCommitParams:
    """Parameters for repos_list_branches_for_head_commit."""
    owner: str
    repo: str
    commit_sha: str

@dataclass
class ReposCreateCommitCommentParams:
    """Parameters for repos_create_commit_comment."""
    owner: str
    repo: str
    commit_sha: str
    body: str
    path: str | None = None
    position: int | None = None
    line: int | None = None

@dataclass
class ReposListCommentsForCommitParams:
    """Parameters for repos_list_comments_for_commit."""
    owner: str
    repo: str
    commit_sha: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposListPullRequestsAssociatedWithCommitParams:
    """Parameters for repos_list_pull_requests_associated_with_commit."""
    owner: str
    repo: str
    commit_sha: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposGetCommitParams:
    """Parameters for repos_get_commit."""
    owner: str
    repo: str
    page: int | None = None
    per_page: int | None = None
    ref: str

@dataclass
class ChecksListForRefParams:
    """Parameters for checks_list_for_ref."""
    owner: str
    repo: str
    ref: str
    check_name: str | None = None
    status: str | None = None
    filter: str | None = None
    per_page: int | None = None
    page: int | None = None
    app_id: int | None = None

@dataclass
class ChecksListSuitesForRefParams:
    """Parameters for checks_list_suites_for_ref."""
    owner: str
    repo: str
    ref: str
    app_id: int | None = None
    check_name: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposGetCombinedStatusForRefParams:
    """Parameters for repos_get_combined_status_for_ref."""
    owner: str
    repo: str
    ref: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposListCommitStatusesForRefParams:
    """Parameters for repos_list_commit_statuses_for_ref."""
    owner: str
    repo: str
    ref: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposGetCommunityProfileMetricsParams:
    """Parameters for repos_get_community_profile_metrics."""
    owner: str
    repo: str

@dataclass
class ReposCompareCommitsParams:
    """Parameters for repos_compare_commits."""
    owner: str
    repo: str
    page: int | None = None
    per_page: int | None = None
    basehead: str

@dataclass
class ReposDeleteFileParams:
    """Parameters for repos_delete_file."""
    owner: str
    repo: str
    path: str
    message: str
    sha: str
    branch: str | None = None
    committer: dict | None = None
    author: dict | None = None

@dataclass
class ReposCreateOrUpdateFileContentsParams:
    """Parameters for repos_create_or_update_file_contents."""
    owner: str
    repo: str
    path: str
    message: str
    content: str
    sha: str | None = None
    branch: str | None = None
    committer: dict | None = None
    author: dict | None = None

@dataclass
class ReposGetContentParams:
    """Parameters for repos_get_content."""
    owner: str
    repo: str
    path: str
    ref: str | None = None

@dataclass
class ReposListContributorsParams:
    """Parameters for repos_list_contributors."""
    owner: str
    repo: str
    anon: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class DependabotListAlertsForRepoParams:
    """Parameters for dependabot_list_alerts_for_repo."""
    owner: str
    repo: str
    state: str | None = None
    severity: str | None = None
    ecosystem: str | None = None
    package: str | None = None
    manifest: str | None = None
    epss_percentage: str | None = None
    has: dict | None = None
    assignee: str | None = None
    scope: str | None = None
    sort: str | None = None
    direction: str | None = None
    before: str | None = None
    after: str | None = None
    per_page: int | None = None

@dataclass
class DependabotUpdateAlertParams:
    """Parameters for dependabot_update_alert."""
    owner: str
    repo: str
    alert_number: int
    state: str | None = None
    dismissed_reason: str | None = None
    dismissed_comment: str | None = None
    assignees: list | None = None

@dataclass
class DependabotGetAlertParams:
    """Parameters for dependabot_get_alert."""
    owner: str
    repo: str
    alert_number: int

@dataclass
class DependabotListRepoSecretsParams:
    """Parameters for dependabot_list_repo_secrets."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class DependabotGetRepoPublicKeyParams:
    """Parameters for dependabot_get_repo_public_key."""
    owner: str
    repo: str

@dataclass
class DependabotDeleteRepoSecretParams:
    """Parameters for dependabot_delete_repo_secret."""
    owner: str
    repo: str
    secret_name: str

@dataclass
class DependabotCreateOrUpdateRepoSecretParams:
    """Parameters for dependabot_create_or_update_repo_secret."""
    owner: str
    repo: str
    secret_name: str
    encrypted_value: str | None = None
    key_id: str | None = None

@dataclass
class DependabotGetRepoSecretParams:
    """Parameters for dependabot_get_repo_secret."""
    owner: str
    repo: str
    secret_name: str

@dataclass
class DependencyGraphDiffRangeParams:
    """Parameters for dependency_graph_diff_range."""
    owner: str
    repo: str
    basehead: str
    name: str | None = None

@dataclass
class DependencyGraphExportSbomParams:
    """Parameters for dependency_graph_export_sbom."""
    owner: str
    repo: str

@dataclass
class DependencyGraphCreateRepositorySnapshotParams:
    """Parameters for dependency_graph_create_repository_snapshot."""
    owner: str
    repo: str
    version: int
    job: dict
    sha: str
    ref: str
    detector: dict
    metadata: dict | None = None
    manifests: dict | None = None
    scanned: str

@dataclass
class ReposCreateDeploymentParams:
    """Parameters for repos_create_deployment."""
    owner: str
    repo: str
    ref: str
    task: str | None = None
    auto_merge: bool | None = None
    required_contexts: list | None = None
    payload: dict | None = None
    environment: str | None = None
    description: str | None = None
    transient_environment: bool | None = None
    production_environment: bool | None = None

@dataclass
class ReposListDeploymentsParams:
    """Parameters for repos_list_deployments."""
    owner: str
    repo: str
    sha: str | None = None
    ref: str | None = None
    task: str | None = None
    environment: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposDeleteDeploymentParams:
    """Parameters for repos_delete_deployment."""
    owner: str
    repo: str
    deployment_id: int

@dataclass
class ReposGetDeploymentParams:
    """Parameters for repos_get_deployment."""
    owner: str
    repo: str
    deployment_id: int

@dataclass
class ReposCreateDeploymentStatusParams:
    """Parameters for repos_create_deployment_status."""
    owner: str
    repo: str
    deployment_id: int
    state: str
    target_url: str | None = None
    log_url: str | None = None
    description: str | None = None
    environment: str | None = None
    environment_url: str | None = None
    auto_inactive: bool | None = None

@dataclass
class ReposListDeploymentStatusesParams:
    """Parameters for repos_list_deployment_statuses."""
    owner: str
    repo: str
    deployment_id: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposGetDeploymentStatusParams:
    """Parameters for repos_get_deployment_status."""
    owner: str
    repo: str
    deployment_id: int
    status_id: int

@dataclass
class ReposCreateDispatchEventParams:
    """Parameters for repos_create_dispatch_event."""
    owner: str
    repo: str
    event_type: str
    client_payload: dict | None = None

@dataclass
class ReposGetAllEnvironmentsParams:
    """Parameters for repos_get_all_environments."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposDeleteAnEnvironmentParams:
    """Parameters for repos_delete_an_environment."""
    owner: str
    repo: str
    environment_name: str

@dataclass
class ReposCreateOrUpdateEnvironmentParams:
    """Parameters for repos_create_or_update_environment."""
    owner: str
    repo: str
    environment_name: str
    wait_timer: int | None = None
    prevent_self_review: bool | None = None
    reviewers: list | None = None
    deployment_branch_policy: dict | None = None

@dataclass
class ReposGetEnvironmentParams:
    """Parameters for repos_get_environment."""
    owner: str
    repo: str
    environment_name: str

@dataclass
class ReposCreateDeploymentBranchPolicyParams:
    """Parameters for repos_create_deployment_branch_policy."""
    owner: str
    repo: str
    environment_name: str
    name: str
    type: str | None = None

@dataclass
class ReposListDeploymentBranchPoliciesParams:
    """Parameters for repos_list_deployment_branch_policies."""
    owner: str
    repo: str
    environment_name: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposDeleteDeploymentBranchPolicyParams:
    """Parameters for repos_delete_deployment_branch_policy."""
    owner: str
    repo: str
    environment_name: str
    branch_policy_id: int

@dataclass
class ReposUpdateDeploymentBranchPolicyParams:
    """Parameters for repos_update_deployment_branch_policy."""
    owner: str
    repo: str
    environment_name: str
    branch_policy_id: int
    name: str

@dataclass
class ReposGetDeploymentBranchPolicyParams:
    """Parameters for repos_get_deployment_branch_policy."""
    owner: str
    repo: str
    environment_name: str
    branch_policy_id: int

@dataclass
class ReposCreateDeploymentProtectionRuleParams:
    """Parameters for repos_create_deployment_protection_rule."""
    environment_name: str
    repo: str
    owner: str
    integration_id: int | None = None

@dataclass
class ReposGetAllDeploymentProtectionRulesParams:
    """Parameters for repos_get_all_deployment_protection_rules."""
    environment_name: str
    repo: str
    owner: str

@dataclass
class ReposListCustomDeploymentRuleIntegrationsParams:
    """Parameters for repos_list_custom_deployment_rule_integrations."""
    environment_name: str
    repo: str
    owner: str
    page: int | None = None
    per_page: int | None = None

@dataclass
class ReposDisableDeploymentProtectionRuleParams:
    """Parameters for repos_disable_deployment_protection_rule."""
    environment_name: str
    repo: str
    owner: str
    protection_rule_id: int

@dataclass
class ReposGetCustomDeploymentProtectionRuleParams:
    """Parameters for repos_get_custom_deployment_protection_rule."""
    owner: str
    repo: str
    environment_name: str
    protection_rule_id: int

@dataclass
class ActionsListEnvironmentSecretsParams:
    """Parameters for actions_list_environment_secrets."""
    owner: str
    repo: str
    environment_name: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActionsGetEnvironmentPublicKeyParams:
    """Parameters for actions_get_environment_public_key."""
    owner: str
    repo: str
    environment_name: str

@dataclass
class ActionsDeleteEnvironmentSecretParams:
    """Parameters for actions_delete_environment_secret."""
    owner: str
    repo: str
    environment_name: str
    secret_name: str

@dataclass
class ActionsCreateOrUpdateEnvironmentSecretParams:
    """Parameters for actions_create_or_update_environment_secret."""
    owner: str
    repo: str
    environment_name: str
    secret_name: str
    encrypted_value: str
    key_id: str

@dataclass
class ActionsGetEnvironmentSecretParams:
    """Parameters for actions_get_environment_secret."""
    owner: str
    repo: str
    environment_name: str
    secret_name: str

@dataclass
class ActionsCreateEnvironmentVariableParams:
    """Parameters for actions_create_environment_variable."""
    owner: str
    repo: str
    environment_name: str
    name: str
    value: str

@dataclass
class ActionsListEnvironmentVariablesParams:
    """Parameters for actions_list_environment_variables."""
    owner: str
    repo: str
    environment_name: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActionsUpdateEnvironmentVariableParams:
    """Parameters for actions_update_environment_variable."""
    owner: str
    repo: str
    name: str
    environment_name: str
    value: str | None = None

@dataclass
class ActionsDeleteEnvironmentVariableParams:
    """Parameters for actions_delete_environment_variable."""
    owner: str
    repo: str
    name: str
    environment_name: str

@dataclass
class ActionsGetEnvironmentVariableParams:
    """Parameters for actions_get_environment_variable."""
    owner: str
    repo: str
    environment_name: str
    name: str

@dataclass
class ActivityListRepoEventsParams:
    """Parameters for activity_list_repo_events."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposCreateForkParams:
    """Parameters for repos_create_fork."""
    owner: str
    repo: str
    organization: str | None = None
    name: str | None = None
    default_branch_only: bool | None = None

@dataclass
class ReposListForksParams:
    """Parameters for repos_list_forks."""
    owner: str
    repo: str
    sort: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class GitCreateBlobParams:
    """Parameters for git_create_blob."""
    owner: str
    repo: str
    content: str
    encoding: str | None = None

@dataclass
class GitGetBlobParams:
    """Parameters for git_get_blob."""
    owner: str
    repo: str
    file_sha: str

@dataclass
class GitCreateCommitParams:
    """Parameters for git_create_commit."""
    owner: str
    repo: str
    message: str
    tree: str
    parents: list | None = None
    author: dict | None = None
    committer: dict | None = None
    signature: str | None = None

@dataclass
class GitGetCommitParams:
    """Parameters for git_get_commit."""
    owner: str
    repo: str
    commit_sha: str

@dataclass
class GitListMatchingRefsParams:
    """Parameters for git_list_matching_refs."""
    owner: str
    repo: str
    ref: str

@dataclass
class GitGetRefParams:
    """Parameters for git_get_ref."""
    owner: str
    repo: str
    ref: str

@dataclass
class GitCreateRefParams:
    """Parameters for git_create_ref."""
    owner: str
    repo: str
    ref: str
    sha: str

@dataclass
class GitUpdateRefParams:
    """Parameters for git_update_ref."""
    owner: str
    repo: str
    ref: str
    sha: str
    force: bool | None = None

@dataclass
class GitDeleteRefParams:
    """Parameters for git_delete_ref."""
    owner: str
    repo: str
    ref: str

@dataclass
class GitCreateTagParams:
    """Parameters for git_create_tag."""
    owner: str
    repo: str
    tag: str
    message: str
    object: str
    type: str
    tagger: dict | None = None

@dataclass
class GitGetTagParams:
    """Parameters for git_get_tag."""
    owner: str
    repo: str
    tag_sha: str

@dataclass
class GitCreateTreeParams:
    """Parameters for git_create_tree."""
    owner: str
    repo: str
    tree: list
    base_tree: str | None = None

@dataclass
class GitGetTreeParams:
    """Parameters for git_get_tree."""
    owner: str
    repo: str
    tree_sha: str
    recursive: str | None = None

@dataclass
class ReposCreateWebhookParams:
    """Parameters for repos_create_webhook."""
    owner: str
    repo: str
    name: str | None = None
    config: dict | None = None
    events: list | None = None
    active: bool | None = None

@dataclass
class ReposListWebhooksParams:
    """Parameters for repos_list_webhooks."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposUpdateWebhookParams:
    """Parameters for repos_update_webhook."""
    owner: str
    repo: str
    hook_id: int
    config: dict | None = None
    events: list | None = None
    add_events: list | None = None
    remove_events: list | None = None
    active: bool | None = None

@dataclass
class ReposDeleteWebhookParams:
    """Parameters for repos_delete_webhook."""
    owner: str
    repo: str
    hook_id: int

@dataclass
class ReposGetWebhookParams:
    """Parameters for repos_get_webhook."""
    owner: str
    repo: str
    hook_id: int

@dataclass
class ReposUpdateWebhookConfigForRepoParams:
    """Parameters for repos_update_webhook_config_for_repo."""
    owner: str
    repo: str
    hook_id: int
    url: str | None = None
    content_type: str | None = None
    secret: str | None = None
    insecure_ssl: dict | None = None

@dataclass
class ReposGetWebhookConfigForRepoParams:
    """Parameters for repos_get_webhook_config_for_repo."""
    owner: str
    repo: str
    hook_id: int

@dataclass
class ReposListWebhookDeliveriesParams:
    """Parameters for repos_list_webhook_deliveries."""
    owner: str
    repo: str
    hook_id: int
    per_page: int | None = None
    cursor: str | None = None

@dataclass
class ReposGetWebhookDeliveryParams:
    """Parameters for repos_get_webhook_delivery."""
    owner: str
    repo: str
    hook_id: int
    delivery_id: int

@dataclass
class ReposRedeliverWebhookDeliveryParams:
    """Parameters for repos_redeliver_webhook_delivery."""
    owner: str
    repo: str
    hook_id: int
    delivery_id: int

@dataclass
class ReposPingWebhookParams:
    """Parameters for repos_ping_webhook."""
    owner: str
    repo: str
    hook_id: int

@dataclass
class ReposTestPushWebhookParams:
    """Parameters for repos_test_push_webhook."""
    owner: str
    repo: str
    hook_id: int

@dataclass
class ReposDisableImmutableReleasesParams:
    """Parameters for repos_disable_immutable_releases."""
    owner: str
    repo: str

@dataclass
class ReposEnableImmutableReleasesParams:
    """Parameters for repos_enable_immutable_releases."""
    owner: str
    repo: str

@dataclass
class ReposCheckImmutableReleasesParams:
    """Parameters for repos_check_immutable_releases."""
    owner: str
    repo: str

@dataclass
class MigrationsUpdateImportParams:
    """Parameters for migrations_update_import."""
    owner: str
    repo: str
    vcs_username: str | None = None
    vcs_password: str | None = None
    vcs: str | None = None
    tfvc_project: str | None = None

@dataclass
class MigrationsCancelImportParams:
    """Parameters for migrations_cancel_import."""
    owner: str
    repo: str

@dataclass
class MigrationsStartImportParams:
    """Parameters for migrations_start_import."""
    owner: str
    repo: str
    vcs_url: str
    vcs: str | None = None
    vcs_username: str | None = None
    vcs_password: str | None = None
    tfvc_project: str | None = None

@dataclass
class MigrationsGetImportStatusParams:
    """Parameters for migrations_get_import_status."""
    owner: str
    repo: str

@dataclass
class MigrationsGetCommitAuthorsParams:
    """Parameters for migrations_get_commit_authors."""
    owner: str
    repo: str
    since: int | None = None

@dataclass
class MigrationsMapCommitAuthorParams:
    """Parameters for migrations_map_commit_author."""
    owner: str
    repo: str
    author_id: int
    email: str | None = None
    name: str | None = None

@dataclass
class MigrationsGetLargeFilesParams:
    """Parameters for migrations_get_large_files."""
    owner: str
    repo: str

@dataclass
class MigrationsSetLfsPreferenceParams:
    """Parameters for migrations_set_lfs_preference."""
    owner: str
    repo: str
    use_lfs: str

@dataclass
class AppsGetRepoInstallationParams:
    """Parameters for apps_get_repo_installation."""
    owner: str
    repo: str

@dataclass
class InteractionsRemoveRestrictionsForRepoParams:
    """Parameters for interactions_remove_restrictions_for_repo."""
    owner: str
    repo: str

@dataclass
class InteractionsSetRestrictionsForRepoParams:
    """Parameters for interactions_set_restrictions_for_repo."""
    owner: str
    repo: str
    limit: str
    expiry: str | None = None

@dataclass
class InteractionsGetRestrictionsForRepoParams:
    """Parameters for interactions_get_restrictions_for_repo."""
    owner: str
    repo: str

@dataclass
class ReposListInvitationsParams:
    """Parameters for repos_list_invitations."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposUpdateInvitationParams:
    """Parameters for repos_update_invitation."""
    owner: str
    repo: str
    invitation_id: int
    permissions: str | None = None

@dataclass
class ReposDeleteInvitationParams:
    """Parameters for repos_delete_invitation."""
    owner: str
    repo: str
    invitation_id: int

@dataclass
class IssuesCreateParams:
    """Parameters for issues_create."""
    owner: str
    repo: str
    title: dict
    body: str | None = None
    assignee: str | None = None
    milestone: dict | None = None
    labels: list | None = None
    assignees: list | None = None
    type: str | None = None

@dataclass
class IssuesListForRepoParams:
    """Parameters for issues_list_for_repo."""
    owner: str
    repo: str
    milestone: str | None = None
    state: str | None = None
    assignee: str | None = None
    type: str | None = None
    creator: str | None = None
    mentioned: str | None = None
    labels: str | None = None
    sort: str | None = None
    direction: str | None = None
    since: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class IssuesListCommentsForRepoParams:
    """Parameters for issues_list_comments_for_repo."""
    owner: str
    repo: str
    sort: str | None = None
    direction: str | None = None
    since: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class IssuesUpdateCommentParams:
    """Parameters for issues_update_comment."""
    owner: str
    repo: str
    comment_id: int
    body: str

@dataclass
class IssuesDeleteCommentParams:
    """Parameters for issues_delete_comment."""
    owner: str
    repo: str
    comment_id: int

@dataclass
class IssuesGetCommentParams:
    """Parameters for issues_get_comment."""
    owner: str
    repo: str
    comment_id: int

@dataclass
class IssuesUnpinCommentParams:
    """Parameters for issues_unpin_comment."""
    owner: str
    repo: str
    comment_id: int

@dataclass
class IssuesPinCommentParams:
    """Parameters for issues_pin_comment."""
    owner: str
    repo: str
    comment_id: int

@dataclass
class ReactionsCreateForIssueCommentParams:
    """Parameters for reactions_create_for_issue_comment."""
    owner: str
    repo: str
    comment_id: int
    content: str

@dataclass
class ReactionsListForIssueCommentParams:
    """Parameters for reactions_list_for_issue_comment."""
    owner: str
    repo: str
    comment_id: int
    content: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReactionsDeleteForIssueCommentParams:
    """Parameters for reactions_delete_for_issue_comment."""
    owner: str
    repo: str
    comment_id: int
    reaction_id: int

@dataclass
class IssuesListEventsForRepoParams:
    """Parameters for issues_list_events_for_repo."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class IssuesGetEventParams:
    """Parameters for issues_get_event."""
    owner: str
    repo: str
    event_id: int

@dataclass
class IssuesUpdateParams:
    """Parameters for issues_update."""
    owner: str
    repo: str
    issue_number: int
    title: dict | None = None
    body: str | None = None
    assignee: str | None = None
    state: str | None = None
    state_reason: str | None = None
    milestone: dict | None = None
    labels: list | None = None
    assignees: list | None = None
    issue_field_values: list | None = None
    type: str | None = None

@dataclass
class IssuesGetParams:
    """Parameters for issues_get."""
    owner: str
    repo: str
    issue_number: int

@dataclass
class IssuesAddAssigneesParams:
    """Parameters for issues_add_assignees."""
    owner: str
    repo: str
    issue_number: int
    assignees: list | None = None

@dataclass
class IssuesRemoveAssigneesParams:
    """Parameters for issues_remove_assignees."""
    owner: str
    repo: str
    issue_number: int
    assignees: list | None = None

@dataclass
class IssuesCheckUserCanBeAssignedToIssueParams:
    """Parameters for issues_check_user_can_be_assigned_to_issue."""
    owner: str
    repo: str
    issue_number: int
    assignee: str

@dataclass
class IssuesCreateCommentParams:
    """Parameters for issues_create_comment."""
    owner: str
    repo: str
    issue_number: int
    body: str

@dataclass
class IssuesListCommentsParams:
    """Parameters for issues_list_comments."""
    owner: str
    repo: str
    issue_number: int
    since: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class IssuesAddBlockedByDependencyParams:
    """Parameters for issues_add_blocked_by_dependency."""
    owner: str
    repo: str
    issue_number: int
    issue_id: int

@dataclass
class IssuesListDependenciesBlockedByParams:
    """Parameters for issues_list_dependencies_blocked_by."""
    owner: str
    repo: str
    issue_number: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class IssuesRemoveDependencyBlockedByParams:
    """Parameters for issues_remove_dependency_blocked_by."""
    owner: str
    repo: str
    issue_number: int
    issue_id: int

@dataclass
class IssuesListDependenciesBlockingParams:
    """Parameters for issues_list_dependencies_blocking."""
    owner: str
    repo: str
    issue_number: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class IssuesListEventsParams:
    """Parameters for issues_list_events."""
    owner: str
    repo: str
    issue_number: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class IssuesListIssueFieldValuesForIssueParams:
    """Parameters for issues_list_issue_field_values_for_issue."""
    owner: str
    repo: str
    issue_number: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class IssuesAddLabelsParams:
    """Parameters for issues_add_labels."""
    owner: str
    repo: str
    issue_number: int
    body: dict | None = None

@dataclass
class IssuesRemoveAllLabelsParams:
    """Parameters for issues_remove_all_labels."""
    owner: str
    repo: str
    issue_number: int

@dataclass
class IssuesSetLabelsParams:
    """Parameters for issues_set_labels."""
    owner: str
    repo: str
    issue_number: int
    body: dict | None = None

@dataclass
class IssuesListLabelsOnIssueParams:
    """Parameters for issues_list_labels_on_issue."""
    owner: str
    repo: str
    issue_number: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class IssuesRemoveLabelParams:
    """Parameters for issues_remove_label."""
    owner: str
    repo: str
    issue_number: int
    name: str

@dataclass
class IssuesUnlockParams:
    """Parameters for issues_unlock."""
    owner: str
    repo: str
    issue_number: int

@dataclass
class IssuesLockParams:
    """Parameters for issues_lock."""
    owner: str
    repo: str
    issue_number: int
    lock_reason: str | None = None

@dataclass
class IssuesGetParentParams:
    """Parameters for issues_get_parent."""
    owner: str
    repo: str
    issue_number: int

@dataclass
class ReactionsCreateForIssueParams:
    """Parameters for reactions_create_for_issue."""
    owner: str
    repo: str
    issue_number: int
    content: str

@dataclass
class ReactionsListForIssueParams:
    """Parameters for reactions_list_for_issue."""
    owner: str
    repo: str
    issue_number: int
    content: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReactionsDeleteForIssueParams:
    """Parameters for reactions_delete_for_issue."""
    owner: str
    repo: str
    issue_number: int
    reaction_id: int

@dataclass
class IssuesRemoveSubIssueParams:
    """Parameters for issues_remove_sub_issue."""
    owner: str
    repo: str
    issue_number: int
    sub_issue_id: int

@dataclass
class IssuesAddSubIssueParams:
    """Parameters for issues_add_sub_issue."""
    owner: str
    repo: str
    issue_number: int
    sub_issue_id: int
    replace_parent: bool | None = None

@dataclass
class IssuesListSubIssuesParams:
    """Parameters for issues_list_sub_issues."""
    owner: str
    repo: str
    issue_number: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class IssuesReprioritizeSubIssueParams:
    """Parameters for issues_reprioritize_sub_issue."""
    owner: str
    repo: str
    issue_number: int
    sub_issue_id: int
    after_id: int | None = None
    before_id: int | None = None

@dataclass
class IssuesListEventsForTimelineParams:
    """Parameters for issues_list_events_for_timeline."""
    owner: str
    repo: str
    issue_number: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposCreateDeployKeyParams:
    """Parameters for repos_create_deploy_key."""
    owner: str
    repo: str
    title: str | None = None
    key: str
    read_only: bool | None = None

@dataclass
class ReposListDeployKeysParams:
    """Parameters for repos_list_deploy_keys."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposDeleteDeployKeyParams:
    """Parameters for repos_delete_deploy_key."""
    owner: str
    repo: str
    key_id: int

@dataclass
class ReposGetDeployKeyParams:
    """Parameters for repos_get_deploy_key."""
    owner: str
    repo: str
    key_id: int

@dataclass
class IssuesCreateLabelParams:
    """Parameters for issues_create_label."""
    owner: str
    repo: str
    name: str
    color: str | None = None
    description: str | None = None

@dataclass
class IssuesListLabelsForRepoParams:
    """Parameters for issues_list_labels_for_repo."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class IssuesUpdateLabelParams:
    """Parameters for issues_update_label."""
    owner: str
    repo: str
    name: str
    new_name: str | None = None
    color: str | None = None
    description: str | None = None

@dataclass
class IssuesDeleteLabelParams:
    """Parameters for issues_delete_label."""
    owner: str
    repo: str
    name: str

@dataclass
class IssuesGetLabelParams:
    """Parameters for issues_get_label."""
    owner: str
    repo: str
    name: str

@dataclass
class ReposListLanguagesParams:
    """Parameters for repos_list_languages."""
    owner: str
    repo: str

@dataclass
class LicensesGetForRepoParams:
    """Parameters for licenses_get_for_repo."""
    owner: str
    repo: str
    ref: str | None = None

@dataclass
class ReposMergeUpstreamParams:
    """Parameters for repos_merge_upstream."""
    owner: str
    repo: str
    branch: str

@dataclass
class ReposMergeParams:
    """Parameters for repos_merge."""
    owner: str
    repo: str
    base: str
    head: str
    commit_message: str | None = None

@dataclass
class IssuesCreateMilestoneParams:
    """Parameters for issues_create_milestone."""
    owner: str
    repo: str
    title: str
    state: str | None = None
    description: str | None = None
    due_on: str | None = None

@dataclass
class IssuesListMilestonesParams:
    """Parameters for issues_list_milestones."""
    owner: str
    repo: str
    state: str | None = None
    sort: str | None = None
    direction: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class IssuesUpdateMilestoneParams:
    """Parameters for issues_update_milestone."""
    owner: str
    repo: str
    milestone_number: int
    title: str | None = None
    state: str | None = None
    description: str | None = None
    due_on: str | None = None

@dataclass
class IssuesDeleteMilestoneParams:
    """Parameters for issues_delete_milestone."""
    owner: str
    repo: str
    milestone_number: int

@dataclass
class IssuesGetMilestoneParams:
    """Parameters for issues_get_milestone."""
    owner: str
    repo: str
    milestone_number: int

@dataclass
class IssuesListLabelsForMilestoneParams:
    """Parameters for issues_list_labels_for_milestone."""
    owner: str
    repo: str
    milestone_number: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActivityMarkRepoNotificationsAsReadParams:
    """Parameters for activity_mark_repo_notifications_as_read."""
    owner: str
    repo: str
    last_read_at: str | None = None

@dataclass
class GetReposByOwnerByRepoNotificationsParams:
    """Parameters for get_repos_by_owner_by_repo_notifications."""
    owner: str
    repo: str
    all: bool | None = None
    participating: bool | None = None
    since: str | None = None
    before: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposCreatePagesSiteParams:
    """Parameters for repos_create_pages_site."""
    owner: str
    repo: str
    build_type: str | None = None
    source: dict | None = None

@dataclass
class ReposDeletePagesSiteParams:
    """Parameters for repos_delete_pages_site."""
    owner: str
    repo: str

@dataclass
class ReposUpdateInformationAboutPagesSiteParams:
    """Parameters for repos_update_information_about_pages_site."""
    owner: str
    repo: str
    cname: str | None = None
    https_enforced: bool | None = None
    build_type: str | None = None
    source: dict | None = None

@dataclass
class ReposGetPagesParams:
    """Parameters for repos_get_pages."""
    owner: str
    repo: str

@dataclass
class ReposRequestPagesBuildParams:
    """Parameters for repos_request_pages_build."""
    owner: str
    repo: str

@dataclass
class ReposListPagesBuildsParams:
    """Parameters for repos_list_pages_builds."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposGetLatestPagesBuildParams:
    """Parameters for repos_get_latest_pages_build."""
    owner: str
    repo: str

@dataclass
class ReposGetPagesBuildParams:
    """Parameters for repos_get_pages_build."""
    owner: str
    repo: str
    build_id: int

@dataclass
class ReposCreatePagesDeploymentParams:
    """Parameters for repos_create_pages_deployment."""
    owner: str
    repo: str
    artifact_id: float | None = None
    artifact_url: str | None = None
    environment: str | None = None
    pages_build_version: str
    oidc_token: str

@dataclass
class ReposGetPagesDeploymentParams:
    """Parameters for repos_get_pages_deployment."""
    owner: str
    repo: str
    pages_deployment_id: dict

@dataclass
class ReposCancelPagesDeploymentParams:
    """Parameters for repos_cancel_pages_deployment."""
    owner: str
    repo: str
    pages_deployment_id: dict

@dataclass
class ReposGetPagesHealthCheckParams:
    """Parameters for repos_get_pages_health_check."""
    owner: str
    repo: str

@dataclass
class ReposDisablePrivateVulnerabilityReportingParams:
    """Parameters for repos_disable_private_vulnerability_reporting."""
    owner: str
    repo: str

@dataclass
class ReposEnablePrivateVulnerabilityReportingParams:
    """Parameters for repos_enable_private_vulnerability_reporting."""
    owner: str
    repo: str

@dataclass
class ReposCheckPrivateVulnerabilityReportingParams:
    """Parameters for repos_check_private_vulnerability_reporting."""
    owner: str
    repo: str

@dataclass
class PatchReposByOwnerByRepoPropertiesValuesParams:
    """Parameters for patch_repos_by_owner_by_repo_properties_values."""
    owner: str
    repo: str
    properties: list

@dataclass
class GetReposByOwnerByRepoPropertiesValuesParams:
    """Parameters for get_repos_by_owner_by_repo_properties_values."""
    owner: str
    repo: str

@dataclass
class PullsCreateParams:
    """Parameters for pulls_create."""
    owner: str
    repo: str
    title: str | None = None
    head: str
    head_repo: str | None = None
    base: str
    body: str | None = None
    maintainer_can_modify: bool | None = None
    draft: bool | None = None
    issue: int | None = None

@dataclass
class PullsListParams:
    """Parameters for pulls_list."""
    owner: str
    repo: str
    state: str | None = None
    head: str | None = None
    base: str | None = None
    sort: str | None = None
    direction: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class PullsListReviewCommentsForRepoParams:
    """Parameters for pulls_list_review_comments_for_repo."""
    owner: str
    repo: str
    sort: str | None = None
    direction: str | None = None
    since: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class PullsUpdateReviewCommentParams:
    """Parameters for pulls_update_review_comment."""
    owner: str
    repo: str
    comment_id: int
    body: str

@dataclass
class PullsDeleteReviewCommentParams:
    """Parameters for pulls_delete_review_comment."""
    owner: str
    repo: str
    comment_id: int

@dataclass
class PullsGetReviewCommentParams:
    """Parameters for pulls_get_review_comment."""
    owner: str
    repo: str
    comment_id: int

@dataclass
class ReactionsCreateForPullRequestReviewCommentParams:
    """Parameters for reactions_create_for_pull_request_review_comment."""
    owner: str
    repo: str
    comment_id: int
    content: str

@dataclass
class ReactionsListForPullRequestReviewCommentParams:
    """Parameters for reactions_list_for_pull_request_review_comment."""
    owner: str
    repo: str
    comment_id: int
    content: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReactionsDeleteForPullRequestCommentParams:
    """Parameters for reactions_delete_for_pull_request_comment."""
    owner: str
    repo: str
    comment_id: int
    reaction_id: int

@dataclass
class PullsUpdateParams:
    """Parameters for pulls_update."""
    owner: str
    repo: str
    pull_number: int
    title: str | None = None
    body: str | None = None
    state: str | None = None
    base: str | None = None
    maintainer_can_modify: bool | None = None

@dataclass
class PullsGetParams:
    """Parameters for pulls_get."""
    owner: str
    repo: str
    pull_number: int

@dataclass
class CodespacesCreateWithPrForAuthenticatedUserParams:
    """Parameters for codespaces_create_with_pr_for_authenticated_user."""
    owner: str
    repo: str
    pull_number: int
    location: str | None = None
    geo: str | None = None
    client_ip: str | None = None
    machine: str | None = None
    devcontainer_path: str | None = None
    multi_repo_permissions_opt_out: bool | None = None
    working_directory: str | None = None
    idle_timeout_minutes: int | None = None
    display_name: str | None = None
    retention_period_minutes: int | None = None

@dataclass
class PullsCreateReviewCommentParams:
    """Parameters for pulls_create_review_comment."""
    owner: str
    repo: str
    pull_number: int
    body: str
    commit_id: str
    path: str
    position: int | None = None
    side: str | None = None
    line: int | None = None
    start_line: int | None = None
    start_side: str | None = None
    in_reply_to: int | None = None
    subject_type: str | None = None

@dataclass
class PullsListReviewCommentsParams:
    """Parameters for pulls_list_review_comments."""
    owner: str
    repo: str
    pull_number: int
    sort: str | None = None
    direction: str | None = None
    since: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class PullsCreateReplyForReviewCommentParams:
    """Parameters for pulls_create_reply_for_review_comment."""
    owner: str
    repo: str
    pull_number: int
    comment_id: int
    body: str

@dataclass
class PullsListCommitsParams:
    """Parameters for pulls_list_commits."""
    owner: str
    repo: str
    pull_number: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class PullsListFilesParams:
    """Parameters for pulls_list_files."""
    owner: str
    repo: str
    pull_number: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class PullsMergeParams:
    """Parameters for pulls_merge."""
    owner: str
    repo: str
    pull_number: int
    commit_title: str | None = None
    commit_message: str | None = None
    sha: str | None = None
    merge_method: str | None = None

@dataclass
class PullsCheckIfMergedParams:
    """Parameters for pulls_check_if_merged."""
    owner: str
    repo: str
    pull_number: int

@dataclass
class PullsRequestReviewersParams:
    """Parameters for pulls_request_reviewers."""
    owner: str
    repo: str
    pull_number: int
    reviewers: list | None = None
    team_reviewers: list | None = None

@dataclass
class PullsRemoveRequestedReviewersParams:
    """Parameters for pulls_remove_requested_reviewers."""
    owner: str
    repo: str
    pull_number: int
    reviewers: list
    team_reviewers: list | None = None

@dataclass
class PullsListRequestedReviewersParams:
    """Parameters for pulls_list_requested_reviewers."""
    owner: str
    repo: str
    pull_number: int

@dataclass
class PullsCreateReviewParams:
    """Parameters for pulls_create_review."""
    owner: str
    repo: str
    pull_number: int
    commit_id: str | None = None
    body: str | None = None
    event: str | None = None
    comments: list | None = None

@dataclass
class PullsListReviewsParams:
    """Parameters for pulls_list_reviews."""
    owner: str
    repo: str
    pull_number: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class PullsDeletePendingReviewParams:
    """Parameters for pulls_delete_pending_review."""
    owner: str
    repo: str
    pull_number: int
    review_id: int

@dataclass
class PullsUpdateReviewParams:
    """Parameters for pulls_update_review."""
    owner: str
    repo: str
    pull_number: int
    review_id: int
    body: str

@dataclass
class PullsGetReviewParams:
    """Parameters for pulls_get_review."""
    owner: str
    repo: str
    pull_number: int
    review_id: int

@dataclass
class PullsListCommentsForReviewParams:
    """Parameters for pulls_list_comments_for_review."""
    owner: str
    repo: str
    pull_number: int
    review_id: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class PullsDismissReviewParams:
    """Parameters for pulls_dismiss_review."""
    owner: str
    repo: str
    pull_number: int
    review_id: int
    message: str
    event: str | None = None

@dataclass
class PullsSubmitReviewParams:
    """Parameters for pulls_submit_review."""
    owner: str
    repo: str
    pull_number: int
    review_id: int
    body: str | None = None
    event: str

@dataclass
class PullsUpdateBranchParams:
    """Parameters for pulls_update_branch."""
    owner: str
    repo: str
    pull_number: int
    expected_head_sha: str | None = None

@dataclass
class ReposGetReadmeParams:
    """Parameters for repos_get_readme."""
    owner: str
    repo: str
    ref: str | None = None

@dataclass
class ReposGetReadmeInDirectoryParams:
    """Parameters for repos_get_readme_in_directory."""
    owner: str
    repo: str
    dir: str
    ref: str | None = None

@dataclass
class ReposCreateReleaseParams:
    """Parameters for repos_create_release."""
    owner: str
    repo: str
    tag_name: str
    target_commitish: str | None = None
    name: str | None = None
    body: str | None = None
    draft: bool | None = None
    prerelease: bool | None = None
    discussion_category_name: str | None = None
    generate_release_notes: bool | None = None
    make_latest: str | None = None

@dataclass
class ReposListReleasesParams:
    """Parameters for repos_list_releases."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposUpdateReleaseAssetParams:
    """Parameters for repos_update_release_asset."""
    owner: str
    repo: str
    asset_id: int
    name: str | None = None
    label: str | None = None
    state: str | None = None

@dataclass
class ReposDeleteReleaseAssetParams:
    """Parameters for repos_delete_release_asset."""
    owner: str
    repo: str
    asset_id: int

@dataclass
class ReposGetReleaseAssetParams:
    """Parameters for repos_get_release_asset."""
    owner: str
    repo: str
    asset_id: int

@dataclass
class ReposGenerateReleaseNotesParams:
    """Parameters for repos_generate_release_notes."""
    owner: str
    repo: str
    tag_name: str
    target_commitish: str | None = None
    previous_tag_name: str | None = None
    configuration_file_path: str | None = None

@dataclass
class ReposGetLatestReleaseParams:
    """Parameters for repos_get_latest_release."""
    owner: str
    repo: str

@dataclass
class ReposGetReleaseByTagParams:
    """Parameters for repos_get_release_by_tag."""
    owner: str
    repo: str
    tag: str

@dataclass
class ReposUpdateReleaseParams:
    """Parameters for repos_update_release."""
    owner: str
    repo: str
    release_id: int
    tag_name: str | None = None
    target_commitish: str | None = None
    name: str | None = None
    body: str | None = None
    draft: bool | None = None
    prerelease: bool | None = None
    make_latest: str | None = None
    discussion_category_name: str | None = None

@dataclass
class ReposDeleteReleaseParams:
    """Parameters for repos_delete_release."""
    owner: str
    repo: str
    release_id: int

@dataclass
class ReposGetReleaseParams:
    """Parameters for repos_get_release."""
    owner: str
    repo: str
    release_id: int

@dataclass
class ReposUploadReleaseAssetParams:
    """Parameters for repos_upload_release_asset."""
    owner: str
    repo: str
    release_id: int
    name: str
    label: str | None = None

@dataclass
class ReposListReleaseAssetsParams:
    """Parameters for repos_list_release_assets."""
    owner: str
    repo: str
    release_id: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReactionsCreateForReleaseParams:
    """Parameters for reactions_create_for_release."""
    owner: str
    repo: str
    release_id: int
    content: str

@dataclass
class ReactionsListForReleaseParams:
    """Parameters for reactions_list_for_release."""
    owner: str
    repo: str
    release_id: int
    content: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReactionsDeleteForReleaseParams:
    """Parameters for reactions_delete_for_release."""
    owner: str
    repo: str
    release_id: int
    reaction_id: int

@dataclass
class ReposGetBranchRulesParams:
    """Parameters for repos_get_branch_rules."""
    owner: str
    repo: str
    branch: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposCreateRepoRulesetParams:
    """Parameters for repos_create_repo_ruleset."""
    owner: str
    repo: str
    name: str
    target: str | None = None
    enforcement: str
    bypass_actors: list | None = None
    conditions: dict | None = None
    rules: list | None = None

@dataclass
class ReposGetRepoRulesetsParams:
    """Parameters for repos_get_repo_rulesets."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None
    includes_parents: bool | None = None
    targets: str | None = None

@dataclass
class ReposGetRepoRuleSuitesParams:
    """Parameters for repos_get_repo_rule_suites."""
    owner: str
    repo: str
    ref: str | None = None
    time_period: str | None = None
    actor_name: str | None = None
    rule_suite_result: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposGetRepoRuleSuiteParams:
    """Parameters for repos_get_repo_rule_suite."""
    owner: str
    repo: str
    rule_suite_id: int

@dataclass
class ReposDeleteRepoRulesetParams:
    """Parameters for repos_delete_repo_ruleset."""
    owner: str
    repo: str
    ruleset_id: int

@dataclass
class ReposUpdateRepoRulesetParams:
    """Parameters for repos_update_repo_ruleset."""
    owner: str
    repo: str
    ruleset_id: int
    name: str | None = None
    target: str | None = None
    enforcement: str | None = None
    bypass_actors: list | None = None
    conditions: dict | None = None
    rules: list | None = None

@dataclass
class ReposGetRepoRulesetParams:
    """Parameters for repos_get_repo_ruleset."""
    owner: str
    repo: str
    ruleset_id: int
    includes_parents: bool | None = None

@dataclass
class ReposGetRepoRulesetHistoryParams:
    """Parameters for repos_get_repo_ruleset_history."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None
    ruleset_id: int

@dataclass
class ReposGetRepoRulesetVersionParams:
    """Parameters for repos_get_repo_ruleset_version."""
    owner: str
    repo: str
    ruleset_id: int
    version_id: int

@dataclass
class SecretScanningListAlertsForRepoParams:
    """Parameters for secret_scanning_list_alerts_for_repo."""
    owner: str
    repo: str
    state: str | None = None
    secret_type: str | None = None
    resolution: str | None = None
    assignee: str | None = None
    sort: str | None = None
    direction: str | None = None
    page: int | None = None
    per_page: int | None = None
    before: str | None = None
    after: str | None = None
    validity: str | None = None
    is_publicly_leaked: bool | None = None
    is_multi_repo: bool | None = None
    hide_secret: bool | None = None

@dataclass
class SecretScanningUpdateAlertParams:
    """Parameters for secret_scanning_update_alert."""
    owner: str
    repo: str
    alert_number: int
    state: str | None = None
    resolution: str | None = None
    resolution_comment: str | None = None
    assignee: str | None = None

@dataclass
class SecretScanningGetAlertParams:
    """Parameters for secret_scanning_get_alert."""
    owner: str
    repo: str
    alert_number: int
    hide_secret: bool | None = None

@dataclass
class SecretScanningListLocationsForAlertParams:
    """Parameters for secret_scanning_list_locations_for_alert."""
    owner: str
    repo: str
    alert_number: int
    page: int | None = None
    per_page: int | None = None

@dataclass
class SecretScanningCreatePushProtectionBypassParams:
    """Parameters for secret_scanning_create_push_protection_bypass."""
    owner: str
    repo: str
    reason: str
    placeholder_id: str

@dataclass
class SecretScanningGetScanHistoryParams:
    """Parameters for secret_scanning_get_scan_history."""
    owner: str
    repo: str

@dataclass
class SecurityAdvisoriesCreateRepositoryAdvisoryParams:
    """Parameters for security_advisories_create_repository_advisory."""
    owner: str
    repo: str
    summary: str
    description: str
    cve_id: str | None = None
    vulnerabilities: list
    cwe_ids: list | None = None
    credits: list | None = None
    severity: str | None = None
    cvss_vector_string: str | None = None
    start_private_fork: bool | None = None

@dataclass
class SecurityAdvisoriesListRepositoryAdvisoriesParams:
    """Parameters for security_advisories_list_repository_advisories."""
    owner: str
    repo: str
    direction: str | None = None
    sort: str | None = None
    before: str | None = None
    after: str | None = None
    per_page: int | None = None
    state: str | None = None

@dataclass
class PostReposByOwnerByRepoSecurityAdvisoriesReportsParams:
    """Parameters for post_repos_by_owner_by_repo_security_advisories_reports."""
    owner: str
    repo: str
    summary: str
    description: str
    vulnerabilities: list | None = None
    cwe_ids: list | None = None
    severity: str | None = None
    cvss_vector_string: str | None = None
    start_private_fork: bool | None = None

@dataclass
class SecurityAdvisoriesUpdateRepositoryAdvisoryParams:
    """Parameters for security_advisories_update_repository_advisory."""
    owner: str
    repo: str
    ghsa_id: str
    summary: str | None = None
    description: str | None = None
    cve_id: str | None = None
    vulnerabilities: list | None = None
    cwe_ids: list | None = None
    credits: list | None = None
    severity: str | None = None
    cvss_vector_string: str | None = None
    state: str | None = None
    collaborating_users: list | None = None
    collaborating_teams: list | None = None

@dataclass
class SecurityAdvisoriesGetRepositoryAdvisoryParams:
    """Parameters for security_advisories_get_repository_advisory."""
    owner: str
    repo: str
    ghsa_id: str

@dataclass
class PostReposByOwnerByRepoSecurityAdvisoriesByGhsaIdCveParams:
    """Parameters for post_repos_by_owner_by_repo_security_advisories_by_ghsa_id_cve."""
    owner: str
    repo: str
    ghsa_id: str

@dataclass
class SecurityAdvisoriesCreateForkParams:
    """Parameters for security_advisories_create_fork."""
    owner: str
    repo: str
    ghsa_id: str

@dataclass
class ActivityListStargazersForRepoParams:
    """Parameters for activity_list_stargazers_for_repo."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposGetCodeFrequencyStatsParams:
    """Parameters for repos_get_code_frequency_stats."""
    owner: str
    repo: str

@dataclass
class ReposGetCommitActivityStatsParams:
    """Parameters for repos_get_commit_activity_stats."""
    owner: str
    repo: str

@dataclass
class ReposGetContributorsStatsParams:
    """Parameters for repos_get_contributors_stats."""
    owner: str
    repo: str

@dataclass
class ReposGetParticipationStatsParams:
    """Parameters for repos_get_participation_stats."""
    owner: str
    repo: str

@dataclass
class ReposGetPunchCardStatsParams:
    """Parameters for repos_get_punch_card_stats."""
    owner: str
    repo: str

@dataclass
class ReposCreateCommitStatusParams:
    """Parameters for repos_create_commit_status."""
    owner: str
    repo: str
    sha: str
    state: str
    target_url: str | None = None
    description: str | None = None
    context: str | None = None

@dataclass
class ActivityListWatchersForRepoParams:
    """Parameters for activity_list_watchers_for_repo."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActivityDeleteRepoSubscriptionParams:
    """Parameters for activity_delete_repo_subscription."""
    owner: str
    repo: str

@dataclass
class ActivitySetRepoSubscriptionParams:
    """Parameters for activity_set_repo_subscription."""
    owner: str
    repo: str
    subscribed: bool | None = None
    ignored: bool | None = None

@dataclass
class ActivityGetRepoSubscriptionParams:
    """Parameters for activity_get_repo_subscription."""
    owner: str
    repo: str

@dataclass
class ReposListTagsParams:
    """Parameters for repos_list_tags."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposDownloadTarballArchiveParams:
    """Parameters for repos_download_tarball_archive."""
    owner: str
    repo: str
    ref: str

@dataclass
class ReposListTeamsParams:
    """Parameters for repos_list_teams."""
    owner: str
    repo: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposReplaceAllTopicsParams:
    """Parameters for repos_replace_all_topics."""
    owner: str
    repo: str
    names: list

@dataclass
class ReposGetAllTopicsParams:
    """Parameters for repos_get_all_topics."""
    owner: str
    repo: str
    page: int | None = None
    per_page: int | None = None

@dataclass
class ReposGetClonesParams:
    """Parameters for repos_get_clones."""
    owner: str
    repo: str
    per: str | None = None

@dataclass
class ReposGetTopPathsParams:
    """Parameters for repos_get_top_paths."""
    owner: str
    repo: str

@dataclass
class ReposGetTopReferrersParams:
    """Parameters for repos_get_top_referrers."""
    owner: str
    repo: str

@dataclass
class ReposGetViewsParams:
    """Parameters for repos_get_views."""
    owner: str
    repo: str
    per: str | None = None

@dataclass
class ReposTransferParams:
    """Parameters for repos_transfer."""
    owner: str
    repo: str
    new_owner: str
    new_name: str | None = None
    team_ids: list | None = None

@dataclass
class ReposDisableVulnerabilityAlertsParams:
    """Parameters for repos_disable_vulnerability_alerts."""
    owner: str
    repo: str

@dataclass
class ReposEnableVulnerabilityAlertsParams:
    """Parameters for repos_enable_vulnerability_alerts."""
    owner: str
    repo: str

@dataclass
class ReposCheckVulnerabilityAlertsParams:
    """Parameters for repos_check_vulnerability_alerts."""
    owner: str
    repo: str

@dataclass
class ReposDownloadZipballArchiveParams:
    """Parameters for repos_download_zipball_archive."""
    owner: str
    repo: str
    ref: str

@dataclass
class ReposCreateUsingTemplateParams:
    """Parameters for repos_create_using_template."""
    template_owner: str
    template_repo: str
    owner: str | None = None
    name: str
    description: str | None = None
    include_all_branches: bool | None = None
    private: bool | None = None

@dataclass
class ReposListPublicParams:
    """Parameters for repos_list_public."""
    since: int | None = None

@dataclass
class IssuesAddIssueFieldValuesParams:
    """Parameters for issues_add_issue_field_values."""
    repository_id: int
    issue_number: int
    issue_field_values: list | None = None

@dataclass
class IssuesSetIssueFieldValuesParams:
    """Parameters for issues_set_issue_field_values."""
    repository_id: int
    issue_number: int
    issue_field_values: list | None = None

@dataclass
class IssuesDeleteIssueFieldValueParams:
    """Parameters for issues_delete_issue_field_value."""
    repository_id: int
    issue_number: int
    issue_field_id: int

@dataclass
class SearchCodeParams:
    """Parameters for search_code."""
    q: str
    sort: str | None = None
    order: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class SearchCommitsParams:
    """Parameters for search_commits."""
    q: str
    sort: str | None = None
    order: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class SearchIssuesAndPullRequestsParams:
    """Parameters for search_issues_and_pull_requests."""
    q: str
    sort: str | None = None
    order: str | None = None
    per_page: int | None = None
    page: int | None = None
    advanced_search: str | None = None

@dataclass
class SearchLabelsParams:
    """Parameters for search_labels."""
    repository_id: int
    q: str
    sort: str | None = None
    order: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class SearchReposParams:
    """Parameters for search_repos."""
    q: str
    sort: str | None = None
    order: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class SearchTopicsParams:
    """Parameters for search_topics."""
    q: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class SearchUsersParams:
    """Parameters for search_users."""
    q: str
    sort: str | None = None
    order: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class TeamsUpdateLegacyParams:
    """Parameters for teams_update_legacy."""
    team_id: int
    name: str
    description: str | None = None
    privacy: str | None = None
    notification_setting: str | None = None
    permission: str | None = None
    parent_team_id: int | None = None

@dataclass
class TeamsDeleteLegacyParams:
    """Parameters for teams_delete_legacy."""
    team_id: int

@dataclass
class TeamsGetLegacyParams:
    """Parameters for teams_get_legacy."""
    team_id: int

@dataclass
class TeamsListPendingInvitationsLegacyParams:
    """Parameters for teams_list_pending_invitations_legacy."""
    team_id: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class TeamsListMembersLegacyParams:
    """Parameters for teams_list_members_legacy."""
    team_id: int
    role: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class TeamsRemoveMemberLegacyParams:
    """Parameters for teams_remove_member_legacy."""
    team_id: int
    username: str

@dataclass
class TeamsAddMemberLegacyParams:
    """Parameters for teams_add_member_legacy."""
    team_id: int
    username: str

@dataclass
class TeamsGetMemberLegacyParams:
    """Parameters for teams_get_member_legacy."""
    team_id: int
    username: str

@dataclass
class TeamsRemoveMembershipForUserLegacyParams:
    """Parameters for teams_remove_membership_for_user_legacy."""
    team_id: int
    username: str

@dataclass
class TeamsAddOrUpdateMembershipForUserLegacyParams:
    """Parameters for teams_add_or_update_membership_for_user_legacy."""
    team_id: int
    username: str
    role: str | None = None

@dataclass
class TeamsGetMembershipForUserLegacyParams:
    """Parameters for teams_get_membership_for_user_legacy."""
    team_id: int
    username: str

@dataclass
class TeamsListReposLegacyParams:
    """Parameters for teams_list_repos_legacy."""
    team_id: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class TeamsRemoveRepoLegacyParams:
    """Parameters for teams_remove_repo_legacy."""
    team_id: int
    owner: str
    repo: str

@dataclass
class TeamsAddOrUpdateRepoPermissionsLegacyParams:
    """Parameters for teams_add_or_update_repo_permissions_legacy."""
    team_id: int
    owner: str
    repo: str
    permission: str | None = None

@dataclass
class TeamsCheckPermissionsForRepoLegacyParams:
    """Parameters for teams_check_permissions_for_repo_legacy."""
    team_id: int
    owner: str
    repo: str

@dataclass
class TeamsListChildLegacyParams:
    """Parameters for teams_list_child_legacy."""
    team_id: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class UsersUpdateAuthenticatedParams:
    """Parameters for users_update_authenticated."""
    name: str | None = None
    email: str | None = None
    blog: str | None = None
    twitter_username: str | None = None
    company: str | None = None
    location: str | None = None
    hireable: bool | None = None
    bio: str | None = None

@dataclass
class UsersListBlockedByAuthenticatedUserParams:
    """Parameters for users_list_blocked_by_authenticated_user."""
    per_page: int | None = None
    page: int | None = None

@dataclass
class UsersUnblockParams:
    """Parameters for users_unblock."""
    username: str

@dataclass
class UsersBlockParams:
    """Parameters for users_block."""
    username: str

@dataclass
class UsersCheckBlockedParams:
    """Parameters for users_check_blocked."""
    username: str

@dataclass
class CodespacesCreateForAuthenticatedUserParams:
    """Parameters for codespaces_create_for_authenticated_user."""
    body: dict

@dataclass
class CodespacesListForAuthenticatedUserParams:
    """Parameters for codespaces_list_for_authenticated_user."""
    per_page: int | None = None
    page: int | None = None
    repository_id: int | None = None

@dataclass
class CodespacesListSecretsForAuthenticatedUserParams:
    """Parameters for codespaces_list_secrets_for_authenticated_user."""
    per_page: int | None = None
    page: int | None = None

@dataclass
class CodespacesDeleteSecretForAuthenticatedUserParams:
    """Parameters for codespaces_delete_secret_for_authenticated_user."""
    secret_name: str

@dataclass
class PutUserCodespacesSecretsBySecretNameParams:
    """Parameters for put_user_codespaces_secrets_by_secret_name."""
    secret_name: str
    encrypted_value: str | None = None
    key_id: str
    selected_repository_ids: list | None = None

@dataclass
class CodespacesGetSecretForAuthenticatedUserParams:
    """Parameters for codespaces_get_secret_for_authenticated_user."""
    secret_name: str

@dataclass
class PutUserCodespacesSecretsBySecretNameRepositoriesParams:
    """Parameters for put_user_codespaces_secrets_by_secret_name_repositories."""
    secret_name: str
    selected_repository_ids: list

@dataclass
class GetUserCodespacesSecretsBySecretNameRepositoriesParams:
    """Parameters for get_user_codespaces_secrets_by_secret_name_repositories."""
    secret_name: str

@dataclass
class DeleteUserCodespacesSecretsBySecretNameRepositoriesByRepositoryIdParams:
    """Parameters for delete_user_codespaces_secrets_by_secret_name_repositories_by_repository_id."""
    secret_name: str
    repository_id: int

@dataclass
class PutUserCodespacesSecretsBySecretNameRepositoriesByRepositoryIdParams:
    """Parameters for put_user_codespaces_secrets_by_secret_name_repositories_by_repository_id."""
    secret_name: str
    repository_id: int

@dataclass
class CodespacesUpdateForAuthenticatedUserParams:
    """Parameters for codespaces_update_for_authenticated_user."""
    codespace_name: str
    machine: str | None = None
    display_name: str | None = None
    recent_folders: list | None = None

@dataclass
class CodespacesDeleteForAuthenticatedUserParams:
    """Parameters for codespaces_delete_for_authenticated_user."""
    codespace_name: str

@dataclass
class CodespacesGetForAuthenticatedUserParams:
    """Parameters for codespaces_get_for_authenticated_user."""
    codespace_name: str

@dataclass
class CodespacesExportForAuthenticatedUserParams:
    """Parameters for codespaces_export_for_authenticated_user."""
    codespace_name: str

@dataclass
class GetUserCodespacesByCodespaceNameExportsByExportIdParams:
    """Parameters for get_user_codespaces_by_codespace_name_exports_by_export_id."""
    codespace_name: str
    export_id: str

@dataclass
class GetUserCodespacesByCodespaceNameMachinesParams:
    """Parameters for get_user_codespaces_by_codespace_name_machines."""
    codespace_name: str

@dataclass
class CodespacesPublishForAuthenticatedUserParams:
    """Parameters for codespaces_publish_for_authenticated_user."""
    codespace_name: str
    name: str | None = None
    private: bool | None = None

@dataclass
class CodespacesStartForAuthenticatedUserParams:
    """Parameters for codespaces_start_for_authenticated_user."""
    codespace_name: str

@dataclass
class CodespacesStopForAuthenticatedUserParams:
    """Parameters for codespaces_stop_for_authenticated_user."""
    codespace_name: str

@dataclass
class PatchUserEmailVisibilityParams:
    """Parameters for patch_user_email_visibility."""
    visibility: str

@dataclass
class UsersAddEmailForAuthenticatedUserParams:
    """Parameters for users_add_email_for_authenticated_user."""
    body: dict | None = None

@dataclass
class UsersDeleteEmailForAuthenticatedUserParams:
    """Parameters for users_delete_email_for_authenticated_user."""
    body: dict

@dataclass
class UsersListEmailsForAuthenticatedUserParams:
    """Parameters for users_list_emails_for_authenticated_user."""
    per_page: int | None = None
    page: int | None = None

@dataclass
class UsersListFollowersForAuthenticatedUserParams:
    """Parameters for users_list_followers_for_authenticated_user."""
    per_page: int | None = None
    page: int | None = None

@dataclass
class UsersListFollowedByAuthenticatedUserParams:
    """Parameters for users_list_followed_by_authenticated_user."""
    per_page: int | None = None
    page: int | None = None

@dataclass
class UsersUnfollowParams:
    """Parameters for users_unfollow."""
    username: str

@dataclass
class UsersFollowParams:
    """Parameters for users_follow."""
    username: str

@dataclass
class UsersCheckPersonIsFollowedByAuthenticatedParams:
    """Parameters for users_check_person_is_followed_by_authenticated."""
    username: str

@dataclass
class UsersCreateGpgKeyForAuthenticatedUserParams:
    """Parameters for users_create_gpg_key_for_authenticated_user."""
    name: str | None = None
    armored_public_key: str

@dataclass
class UsersListGpgKeysForAuthenticatedUserParams:
    """Parameters for users_list_gpg_keys_for_authenticated_user."""
    per_page: int | None = None
    page: int | None = None

@dataclass
class UsersDeleteGpgKeyForAuthenticatedUserParams:
    """Parameters for users_delete_gpg_key_for_authenticated_user."""
    gpg_key_id: int

@dataclass
class UsersGetGpgKeyForAuthenticatedUserParams:
    """Parameters for users_get_gpg_key_for_authenticated_user."""
    gpg_key_id: int

@dataclass
class AppsListInstallationsForAuthenticatedUserParams:
    """Parameters for apps_list_installations_for_authenticated_user."""
    per_page: int | None = None
    page: int | None = None

@dataclass
class GetUserInstallationsByInstallationIdRepositoriesParams:
    """Parameters for get_user_installations_by_installation_id_repositories."""
    installation_id: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class DeleteUserInstallationsByInstallationIdRepositoriesByRepositoryIdParams:
    """Parameters for delete_user_installations_by_installation_id_repositories_by_repository_id."""
    installation_id: int
    repository_id: int

@dataclass
class PutUserInstallationsByInstallationIdRepositoriesByRepositoryIdParams:
    """Parameters for put_user_installations_by_installation_id_repositories_by_repository_id."""
    installation_id: int
    repository_id: int

@dataclass
class PutUserInteractionLimitsParams:
    """Parameters for put_user_interaction_limits."""
    limit: str
    expiry: str | None = None

@dataclass
class IssuesListForAuthenticatedUserParams:
    """Parameters for issues_list_for_authenticated_user."""
    filter: str | None = None
    state: str | None = None
    labels: str | None = None
    sort: str | None = None
    direction: str | None = None
    since: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class PostUserKeysParams:
    """Parameters for post_user_keys."""
    title: str | None = None
    key: str

@dataclass
class UsersListPublicSshKeysForAuthenticatedUserParams:
    """Parameters for users_list_public_ssh_keys_for_authenticated_user."""
    per_page: int | None = None
    page: int | None = None

@dataclass
class DeleteUserKeysByKeyIdParams:
    """Parameters for delete_user_keys_by_key_id."""
    key_id: int

@dataclass
class UsersGetPublicSshKeyForAuthenticatedUserParams:
    """Parameters for users_get_public_ssh_key_for_authenticated_user."""
    key_id: int

@dataclass
class AppsListSubscriptionsForAuthenticatedUserParams:
    """Parameters for apps_list_subscriptions_for_authenticated_user."""
    per_page: int | None = None
    page: int | None = None

@dataclass
class GetUserMarketplacePurchasesStubbedParams:
    """Parameters for get_user_marketplace_purchases_stubbed."""
    per_page: int | None = None
    page: int | None = None

@dataclass
class OrgsListMembershipsForAuthenticatedUserParams:
    """Parameters for orgs_list_memberships_for_authenticated_user."""
    state: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class OrgsUpdateMembershipForAuthenticatedUserParams:
    """Parameters for orgs_update_membership_for_authenticated_user."""
    org: str
    state: str

@dataclass
class OrgsGetMembershipForAuthenticatedUserParams:
    """Parameters for orgs_get_membership_for_authenticated_user."""
    org: str

@dataclass
class MigrationsStartForAuthenticatedUserParams:
    """Parameters for migrations_start_for_authenticated_user."""
    lock_repositories: bool | None = None
    exclude_metadata: bool | None = None
    exclude_git_data: bool | None = None
    exclude_attachments: bool | None = None
    exclude_releases: bool | None = None
    exclude_owner_projects: bool | None = None
    org_metadata_only: bool | None = None
    exclude: list | None = None
    repositories: list

@dataclass
class MigrationsListForAuthenticatedUserParams:
    """Parameters for migrations_list_for_authenticated_user."""
    per_page: int | None = None
    page: int | None = None

@dataclass
class MigrationsGetStatusForAuthenticatedUserParams:
    """Parameters for migrations_get_status_for_authenticated_user."""
    migration_id: int
    exclude: list | None = None

@dataclass
class MigrationsDeleteArchiveForAuthenticatedUserParams:
    """Parameters for migrations_delete_archive_for_authenticated_user."""
    migration_id: int

@dataclass
class MigrationsGetArchiveForAuthenticatedUserParams:
    """Parameters for migrations_get_archive_for_authenticated_user."""
    migration_id: int

@dataclass
class MigrationsUnlockRepoForAuthenticatedUserParams:
    """Parameters for migrations_unlock_repo_for_authenticated_user."""
    migration_id: int
    repo_name: str

@dataclass
class MigrationsListReposForAuthenticatedUserParams:
    """Parameters for migrations_list_repos_for_authenticated_user."""
    migration_id: int
    per_page: int | None = None
    page: int | None = None

@dataclass
class OrgsListForAuthenticatedUserParams:
    """Parameters for orgs_list_for_authenticated_user."""
    per_page: int | None = None
    page: int | None = None

@dataclass
class PackagesListPackagesForAuthenticatedUserParams:
    """Parameters for packages_list_packages_for_authenticated_user."""
    package_type: str
    visibility: str | None = None
    page: int | None = None
    per_page: int | None = None

@dataclass
class PackagesDeletePackageForAuthenticatedUserParams:
    """Parameters for packages_delete_package_for_authenticated_user."""
    package_type: str
    package_name: str

@dataclass
class PackagesGetPackageForAuthenticatedUserParams:
    """Parameters for packages_get_package_for_authenticated_user."""
    package_type: str
    package_name: str

@dataclass
class PackagesRestorePackageForAuthenticatedUserParams:
    """Parameters for packages_restore_package_for_authenticated_user."""
    package_type: str
    package_name: str
    token: str | None = None

@dataclass
class GetUserPackagesByPackageTypeByPackageNameVersionsParams:
    """Parameters for get_user_packages_by_package_type_by_package_name_versions."""
    package_type: str
    package_name: str
    page: int | None = None
    per_page: int | None = None
    state: str | None = None

@dataclass
class DeleteUserPackagesByPackageTypeByPackageNameVersionsByPackageVersionIdParams:
    """Parameters for delete_user_packages_by_package_type_by_package_name_versions_by_package_version_id."""
    package_type: str
    package_name: str
    package_version_id: int

@dataclass
class GetUserPackagesByPackageTypeByPackageNameVersionsByPackageVersionIdParams:
    """Parameters for get_user_packages_by_package_type_by_package_name_versions_by_package_version_id."""
    package_type: str
    package_name: str
    package_version_id: int

@dataclass
class PostUserPackagesByPackageTypeByPackageNameVersionsByPackageVersionIdRestoreParams:
    """Parameters for post_user_packages_by_package_type_by_package_name_versions_by_package_version_id_restore."""
    package_type: str
    package_name: str
    package_version_id: int

@dataclass
class UsersListPublicEmailsForAuthenticatedUserParams:
    """Parameters for users_list_public_emails_for_authenticated_user."""
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposCreateForAuthenticatedUserParams:
    """Parameters for repos_create_for_authenticated_user."""
    name: str
    description: str | None = None
    homepage: str | None = None
    private: bool | None = None
    has_issues: bool | None = None
    has_projects: bool | None = None
    has_wiki: bool | None = None
    has_discussions: bool | None = None
    team_id: int | None = None
    auto_init: bool | None = None
    gitignore_template: str | None = None
    license_template: str | None = None
    allow_squash_merge: bool | None = None
    allow_merge_commit: bool | None = None
    allow_rebase_merge: bool | None = None
    allow_auto_merge: bool | None = None
    delete_branch_on_merge: bool | None = None
    squash_merge_commit_title: str | None = None
    squash_merge_commit_message: str | None = None
    merge_commit_title: str | None = None
    merge_commit_message: str | None = None
    has_downloads: bool | None = None
    is_template: bool | None = None

@dataclass
class ReposListForAuthenticatedUserParams:
    """Parameters for repos_list_for_authenticated_user."""
    visibility: str | None = None
    affiliation: str | None = None
    type: str | None = None
    sort: str | None = None
    direction: str | None = None
    per_page: int | None = None
    page: int | None = None
    since: str | None = None
    before: str | None = None

@dataclass
class ReposListInvitationsForAuthenticatedUserParams:
    """Parameters for repos_list_invitations_for_authenticated_user."""
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposAcceptInvitationForAuthenticatedUserParams:
    """Parameters for repos_accept_invitation_for_authenticated_user."""
    invitation_id: int

@dataclass
class ReposDeclineInvitationForAuthenticatedUserParams:
    """Parameters for repos_decline_invitation_for_authenticated_user."""
    invitation_id: int

@dataclass
class UsersAddSocialAccountForAuthenticatedUserParams:
    """Parameters for users_add_social_account_for_authenticated_user."""
    account_urls: list

@dataclass
class DeleteUserSocialAccountsParams:
    """Parameters for delete_user_social_accounts."""
    account_urls: list

@dataclass
class UsersListSocialAccountsForAuthenticatedUserParams:
    """Parameters for users_list_social_accounts_for_authenticated_user."""
    per_page: int | None = None
    page: int | None = None

@dataclass
class PostUserSshSigningKeysParams:
    """Parameters for post_user_ssh_signing_keys."""
    title: str | None = None
    key: str

@dataclass
class GetUserSshSigningKeysParams:
    """Parameters for get_user_ssh_signing_keys."""
    per_page: int | None = None
    page: int | None = None

@dataclass
class DeleteUserSshSigningKeysBySshSigningKeyIdParams:
    """Parameters for delete_user_ssh_signing_keys_by_ssh_signing_key_id."""
    ssh_signing_key_id: int

@dataclass
class UsersGetSshSigningKeyForAuthenticatedUserParams:
    """Parameters for users_get_ssh_signing_key_for_authenticated_user."""
    ssh_signing_key_id: int

@dataclass
class ActivityListReposStarredByAuthenticatedUserParams:
    """Parameters for activity_list_repos_starred_by_authenticated_user."""
    sort: str | None = None
    direction: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActivityUnstarRepoForAuthenticatedUserParams:
    """Parameters for activity_unstar_repo_for_authenticated_user."""
    owner: str
    repo: str

@dataclass
class ActivityStarRepoForAuthenticatedUserParams:
    """Parameters for activity_star_repo_for_authenticated_user."""
    owner: str
    repo: str

@dataclass
class GetUserStarredByOwnerByRepoParams:
    """Parameters for get_user_starred_by_owner_by_repo."""
    owner: str
    repo: str

@dataclass
class GetUserSubscriptionsParams:
    """Parameters for get_user_subscriptions."""
    per_page: int | None = None
    page: int | None = None

@dataclass
class TeamsListForAuthenticatedUserParams:
    """Parameters for teams_list_for_authenticated_user."""
    per_page: int | None = None
    page: int | None = None

@dataclass
class UsersGetByIdParams:
    """Parameters for users_get_by_id."""
    account_id: int

@dataclass
class ProjectsCreateDraftItemForAuthenticatedUserParams:
    """Parameters for projects_create_draft_item_for_authenticated_user."""
    user_id: str
    project_number: int
    title: str
    body: str | None = None

@dataclass
class UsersListParams:
    """Parameters for users_list."""
    since: int | None = None
    per_page: int | None = None

@dataclass
class ProjectsCreateViewForUserParams:
    """Parameters for projects_create_view_for_user."""
    user_id: str
    project_number: int
    name: str
    layout: str
    filter: str | None = None
    visible_fields: list | None = None

@dataclass
class UsersGetByUsernameParams:
    """Parameters for users_get_by_username."""
    username: str

@dataclass
class UsersListAttestationsBulkParams:
    """Parameters for users_list_attestations_bulk."""
    per_page: int | None = None
    before: str | None = None
    after: str | None = None
    username: str
    subject_digests: list
    predicate_type: str | None = None

@dataclass
class UsersDeleteAttestationsBulkParams:
    """Parameters for users_delete_attestations_bulk."""
    username: str
    body: dict

@dataclass
class UsersDeleteAttestationsBySubjectDigestParams:
    """Parameters for users_delete_attestations_by_subject_digest."""
    username: str
    subject_digest: str

@dataclass
class UsersDeleteAttestationsByIdParams:
    """Parameters for users_delete_attestations_by_id."""
    username: str
    attestation_id: int

@dataclass
class UsersListAttestationsParams:
    """Parameters for users_list_attestations."""
    per_page: int | None = None
    before: str | None = None
    after: str | None = None
    username: str
    subject_digest: str
    predicate_type: str | None = None

@dataclass
class GetUsersByUsernameDockerConflictsParams:
    """Parameters for get_users_by_username_docker_conflicts."""
    username: str

@dataclass
class ActivityListEventsForAuthenticatedUserParams:
    """Parameters for activity_list_events_for_authenticated_user."""
    username: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActivityListOrgEventsForAuthenticatedUserParams:
    """Parameters for activity_list_org_events_for_authenticated_user."""
    username: str
    org: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActivityListPublicEventsForUserParams:
    """Parameters for activity_list_public_events_for_user."""
    username: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class UsersListFollowersForUserParams:
    """Parameters for users_list_followers_for_user."""
    username: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class UsersListFollowingForUserParams:
    """Parameters for users_list_following_for_user."""
    username: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class UsersCheckFollowingForUserParams:
    """Parameters for users_check_following_for_user."""
    username: str
    target_user: str

@dataclass
class GistsListForUserParams:
    """Parameters for gists_list_for_user."""
    username: str
    since: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class UsersListGpgKeysForUserParams:
    """Parameters for users_list_gpg_keys_for_user."""
    username: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class UsersGetContextForUserParams:
    """Parameters for users_get_context_for_user."""
    username: str
    subject_type: str | None = None
    subject_id: str | None = None

@dataclass
class AppsGetUserInstallationParams:
    """Parameters for apps_get_user_installation."""
    username: str

@dataclass
class UsersListPublicKeysForUserParams:
    """Parameters for users_list_public_keys_for_user."""
    username: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class OrgsListForUserParams:
    """Parameters for orgs_list_for_user."""
    username: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class PackagesListPackagesForUserParams:
    """Parameters for packages_list_packages_for_user."""
    package_type: str
    visibility: str | None = None
    username: str
    page: int | None = None
    per_page: int | None = None

@dataclass
class PackagesDeletePackageForUserParams:
    """Parameters for packages_delete_package_for_user."""
    package_type: str
    package_name: str
    username: str

@dataclass
class PackagesGetPackageForUserParams:
    """Parameters for packages_get_package_for_user."""
    package_type: str
    package_name: str
    username: str

@dataclass
class PackagesRestorePackageForUserParams:
    """Parameters for packages_restore_package_for_user."""
    package_type: str
    package_name: str
    username: str
    token: str | None = None

@dataclass
class GetUsersByUsernamePackagesByPackageTypeByPackageNameVersionsParams:
    """Parameters for get_users_by_username_packages_by_package_type_by_package_name_versions."""
    package_type: str
    package_name: str
    username: str

@dataclass
class PackagesDeletePackageVersionForUserParams:
    """Parameters for packages_delete_package_version_for_user."""
    package_type: str
    package_name: str
    username: str
    package_version_id: int

@dataclass
class PackagesGetPackageVersionForUserParams:
    """Parameters for packages_get_package_version_for_user."""
    package_type: str
    package_name: str
    package_version_id: int
    username: str

@dataclass
class PackagesRestorePackageVersionForUserParams:
    """Parameters for packages_restore_package_version_for_user."""
    package_type: str
    package_name: str
    username: str
    package_version_id: int

@dataclass
class ProjectsListForUserParams:
    """Parameters for projects_list_for_user."""
    username: str
    q: str | None = None
    before: str | None = None
    after: str | None = None
    per_page: int | None = None

@dataclass
class ProjectsGetForUserParams:
    """Parameters for projects_get_for_user."""
    project_number: int
    username: str

@dataclass
class ProjectsAddFieldForUserParams:
    """Parameters for projects_add_field_for_user."""
    username: str
    project_number: int
    body: dict

@dataclass
class ProjectsListFieldsForUserParams:
    """Parameters for projects_list_fields_for_user."""
    project_number: int
    username: str
    per_page: int | None = None
    before: str | None = None
    after: str | None = None

@dataclass
class ProjectsGetFieldForUserParams:
    """Parameters for projects_get_field_for_user."""
    project_number: int
    field_id: int
    username: str

@dataclass
class ProjectsAddItemForUserParams:
    """Parameters for projects_add_item_for_user."""
    username: str
    project_number: int
    type: str
    id: int | None = None
    owner: str | None = None
    repo: str | None = None
    number: int | None = None

@dataclass
class ProjectsListItemsForUserParams:
    """Parameters for projects_list_items_for_user."""
    project_number: int
    username: str
    before: str | None = None
    after: str | None = None
    per_page: int | None = None
    q: str | None = None
    fields: dict | None = None

@dataclass
class ProjectsUpdateItemForUserParams:
    """Parameters for projects_update_item_for_user."""
    project_number: int
    username: str
    item_id: int
    fields: list

@dataclass
class ProjectsDeleteItemForUserParams:
    """Parameters for projects_delete_item_for_user."""
    project_number: int
    username: str
    item_id: int

@dataclass
class ProjectsGetUserItemParams:
    """Parameters for projects_get_user_item."""
    project_number: int
    username: str
    item_id: int
    fields: dict | None = None

@dataclass
class ProjectsListViewItemsForUserParams:
    """Parameters for projects_list_view_items_for_user."""
    project_number: int
    username: str
    view_number: int
    fields: dict | None = None
    before: str | None = None
    after: str | None = None
    per_page: int | None = None

@dataclass
class ActivityListReceivedEventsForUserParams:
    """Parameters for activity_list_received_events_for_user."""
    username: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActivityListReceivedPublicEventsForUserParams:
    """Parameters for activity_list_received_public_events_for_user."""
    username: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ReposListForUserParams:
    """Parameters for repos_list_for_user."""
    username: str
    type: str | None = None
    sort: str | None = None
    direction: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class GetUsersByUsernameSettingsBillingPremiumRequestUsageParams:
    """Parameters for get_users_by_username_settings_billing_premium_request_usage."""
    username: str
    year: int | None = None
    month: int | None = None
    day: int | None = None
    model: str | None = None
    product: str | None = None

@dataclass
class BillingGetGithubBillingUsageReportUserParams:
    """Parameters for billing_get_github_billing_usage_report_user."""
    username: str
    year: int | None = None
    month: int | None = None
    day: int | None = None

@dataclass
class GetUsersByUsernameSettingsBillingUsageSummaryParams:
    """Parameters for get_users_by_username_settings_billing_usage_summary."""
    username: str
    year: int | None = None
    month: int | None = None
    day: int | None = None
    repository: str | None = None
    product: str | None = None
    sku: str | None = None

@dataclass
class UsersListSocialAccountsForUserParams:
    """Parameters for users_list_social_accounts_for_user."""
    username: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class UsersListSshSigningKeysForUserParams:
    """Parameters for users_list_ssh_signing_keys_for_user."""
    username: str
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActivityListReposStarredByUserParams:
    """Parameters for activity_list_repos_starred_by_user."""
    username: str
    sort: str | None = None
    direction: str | None = None
    per_page: int | None = None
    page: int | None = None

@dataclass
class ActivityListReposWatchedByUserParams:
    """Parameters for activity_list_repos_watched_by_user."""
    username: str
    per_page: int | None = None
    page: int | None = None

